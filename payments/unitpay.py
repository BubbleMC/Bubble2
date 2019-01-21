import hashlib

from enum import Enum
from urllib import parse
from decimal import Decimal

from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from django.db import transaction, IntegrityError

from payments.models import Payment, Task
from payments.handlers import AggregatorHandler


class UnitPayAggregator(AggregatorHandler):
    class Method(Enum):
        CHECK = 'check'
        PAY = 'pay'

    def __init__(self, request, aggregator):
        super(UnitPayAggregator, self).__init__(request, aggregator)

        self.required_params = {
            'method',
            'params[account]',
            'params[signature]',
            'params[unitpayId]',
            'params[orderSum]',
            'params[orderCurrency]'
        }

    def _get_sign_string(self):
        query_string = self.request.META.get('QUERY_STRING')
        params = parse.parse_qsl(query_string, keep_blank_values=True)
        params.sort()

        sign_string = ''.join(v + '{up}' if 'sign' not in k else '' for k, v in params)
        sign_string += self.aggregator.secret_key

        return hashlib.sha256(sign_string.encode('utf-8')).hexdigest()

    def _read_necessary_data(self):
        try:
            self.method = self.Method(self.data.get('method'))
            self.sign = self.data.get('params[signature]')
            self.payment_id = int(self.data.get('params[unitpayId]'))
            self.cart_id = int(self.data.get('params[account]'))
            self.currency = self.data.get('params[orderCurrency]')
            self.payment_sum = Decimal(self.data.get('params[orderSum]').replace(',', '.'))
        except ValueError:
            self._raise_error('Invalid parameters')

    def _send_error(self, message):
        return JsonResponse({'error': {'message': message}})

    def _send_success(self, message):
        return JsonResponse({'result': {'message': message}})

    @transaction.atomic
    def payment(self):
        try:
            self._check_required_params_exist()
            self._read_necessary_data()

            self._validate_sign(self.sign)

            if self.method == self.Method.CHECK:
                self._check_existence_payment(self.payment_id)
                user_cart = self._get_cart_or_exception(self.cart_id)

                self._validate_currency(self.currency)
                self._validate_price(self.payment_sum, user_cart.price)

                try:
                    with transaction.atomic():
                        Payment(
                            number=self.payment_id,
                            aggregator=self.aggregator,
                            cart=user_cart,
                        ).save()

                        return self._send_success('Check is successful')
                except IntegrityError:
                    self._raise_error('Unable to create payment in database')

            if self.method == self.Method.PAY:
                payment = self._get_payment_or_exception(self.payment_id)
                user_cart = self._get_cart_or_exception(self.cart_id)

                if payment.status:
                    self._raise_error('Payment has already been paid')

                try:
                    with transaction.atomic():
                        payment.status = True
                        payment.completed_date = timezone.now()
                        payment.save()

                        Task(
                            payment=payment,
                            cart=user_cart,
                        ).save()

                        return self._send_success('Pay is successful')
                except IntegrityError:
                    self._raise_error('Unable to create task or save payments status in database')
        except AggregatorHandler.ErrorException as e:
            return self._send_error(e.message)

    def redirect(self):
        # TODO. Need to implement session structure...
        return HttpResponse('OK')
