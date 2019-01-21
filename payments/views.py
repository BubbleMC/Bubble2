from django.http import HttpResponse
from django.views import View

from django.utils.translation import gettext as _

from payments.models import Aggregator
from payments.mixins import PaymentMixin
from payments.unitpay import UnitPayAggregator


class PaymentView(PaymentMixin, View):
    redirect = False

    def get(self, request, aggregator=None, number=None):
        super(PaymentView, self).get(request, aggregator, number)

        if not self.redirect and self.trusted_ips_verification_enable():
            self.trusted_ips_verification()

        if self.aggregator_platform == Aggregator.UNITPAY:
            unitpay_aggregator = UnitPayAggregator(request=request, aggregator=self.aggregator)
            return unitpay_aggregator.redirect() if self.redirect else unitpay_aggregator.payment()
        elif self.aggregator_platform == Aggregator.FREE_KASSA:
            pass
        else:
            pass


def test(request, aggregator=None, number=None):
    return HttpResponse('OK {} {}'.format(aggregator, number))
