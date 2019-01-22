from django.test import TestCase

from payments.models import Aggregator, TrustedIP
from payments.forms import AggregatorForm


class ModelsTestCase(TestCase):
    public_key = '123'
    secret_key = '321'
    ip_address = '127.0.0.1'

    def setUp(self):
        self.trusted_ip = TrustedIP.objects.create(
            ip=self.ip_address
        )

    def test_trusted_ip_validation_error(self):
        form = AggregatorForm({
            'platform': Aggregator.UNITPAY,
            'public_key': self.public_key,
            'secret_key': self.secret_key,
            'trusted_ips_verification': True
        })

        self.assertFalse(form.is_valid())

    def test_trusted_ip_list(self):
        form = AggregatorForm({
            'platform': Aggregator.UNITPAY,
            'public_key': self.public_key,
            'secret_key': self.secret_key,
            'trusted_ips_verification': True,
            'trusted_ips_list': [self.trusted_ip]
        })

        self.assertTrue(form.is_valid())
