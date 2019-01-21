from shop.models import cart
from payments.models import Payment


class AggregatorHandler:
    class ErrorException(Exception):
        def __init__(self, message):
            self.message = message

    required_params = []

    def __init__(self, request, aggregator):
        self.request = request
        self.aggregator = aggregator
        self.data = request.GET.copy()

    def _get_sign_string(self):
        raise NotImplementedError()

    def _read_necessary_data(self):
        raise NotImplementedError()

    def _send_error(self, message):
        raise NotImplementedError()

    def _send_success(self, message):
        raise NotImplementedError()

    def payment(self):
        raise NotImplementedError()

    def redirect(self):
        raise NotImplementedError()

    def _check_existence_payment(self, payment_id):
        if Payment.objects.filter(number=payment_id).exists():
            self._raise_error('Payment already exists')

    def _get_payment_or_exception(self, payment_id):
        try:
            return Payment.objects.get(number=payment_id)
        except Payment.DoesNotExist:
            self._raise_error('Payment not found')

    def _get_cart_or_exception(self, cart_id):
        try:
            return cart.Cart.objects.get(id=cart_id)
        except cart.Cart.DoesNotExist:
            self._raise_error('Invalid cart for payment')

    def _check_required_params_exist(self):
        if any(required_param not in self.data for required_param in self.required_params):
            self._raise_error('Invalid request')

    def _validate_sign(self, sign):
        if sign != self._get_sign_string():
            self._raise_error('Incorrect digital signature')

    def _validate_currency(self, currency):
        if self.aggregator.currency != currency:
            self._raise_error('Invalid payment currency')

    def _validate_price(self, cur_price, rly_price):
        if cur_price != rly_price:
            self._raise_error('Invalid payment amount')

    def _raise_error(self, message):
        raise AggregatorHandler.ErrorException(message)
