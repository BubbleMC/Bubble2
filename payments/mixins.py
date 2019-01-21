from django.http import Http404

from django.utils.translation import gettext as _

from payments.models import Aggregator


class PaymentMixin:
    aggregator_platform = Aggregator.UNITPAY
    aggregator_number = None
    aggregator = None
    request = None

    def get(self, request, aggregator=None, number=None):
        aggregator = aggregator.upper()
        if aggregator is not None and aggregator not in dict(Aggregator.AGGREGATOR_PLATFORM_CHOICES):
            raise Http404(_('Aggregator {} not found'.format(aggregator)))

        self.request = request
        self.aggregator_platform = aggregator
        self.aggregator_number = number

        try:
            self.aggregator = self.get_aggregator()
        except Aggregator.DoesNotExist:
            raise Http404(_('{} aggregator not configured'.format(self.aggregator_platform)))

    def get_ip(self):
        ip = self.request.META.get('HTTP_CF_CONNECTING_IP')
        if ip is None:
            ip = self.request.META.get('REMOTE_ADDR')

        return ip

    def get_aggregator(self):
        filters = {'platform': self.aggregator_platform}
        if self.aggregator_number:
            filters['id'] = self.aggregator_number

        return Aggregator.objects.filter(**filters).first()

    def trusted_ips_verification_enable(self):
        return self.aggregator.trusted_ips_verification

    def trusted_ips_verification(self):
        if not self.aggregator.trusted_ips_list.filter(ip=self.get_ip()).exists():
            raise Http404(_('Your IP does not exist in trusted IPs list'))
