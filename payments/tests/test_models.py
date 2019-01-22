from django.test import TestCase

from payments.models import Aggregator, TrustedIP


class ModelsTestCase(TestCase):
    public_key = '123'
    secret_key = '321'
    ip_address = '127.0.0.1'

    def setUp(self):
        Aggregator.objects.create(
            platform=Aggregator.UNITPAY,
            public_key=self.public_key,
            secret_key=self.secret_key
        )
        TrustedIP.objects.create(
            ip=self.ip_address
        )

    def test_trusted_ip_str(self):
        trusted_ip = TrustedIP.objects.get(ip=self.ip_address)

        self.assertEqual(trusted_ip.__str__(), str(trusted_ip.ip))

    def test_aggregator_str(self):
        aggregator_ = Aggregator.objects.get(public_key=self.public_key)

        str = '{}({})'.format(aggregator_.get_platform_display(), aggregator_.public_key)

        self.assertEqual(aggregator_.__str__(), str)
