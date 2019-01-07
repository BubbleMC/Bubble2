from django.db import models
from django.utils import timezone

from django.utils.translation import gettext as _


from shop.models.cart import Cart


class TrustedIP(models.Model):
    class Meta:
        db_table = 'trusted_ip'
        verbose_name = _('Trusted IP')
        verbose_name_plural = _('Trusted IPs')

    ip = models.GenericIPAddressField(
        verbose_name=_('IP')
    )

    def __str__(self):
        return self.ip


class Aggregator(models.Model):
    class Meta:
        db_table = 'aggregator'
        verbose_name = _('Aggregator')
        verbose_name_plural = _('Aggregators')

    UNITPAY = 'UP'
    FREE_KASSA = 'FK'
    INTER_KASSA = 'IK'

    AGGREGATOR_PLATFORM_CHOICES = (
        (UNITPAY, _('UnitPay')),
        (FREE_KASSA, _('Free-Kassa')),
        (INTER_KASSA, _('InterKassa')),
    )

    platform = models.CharField(
        max_length=2,
        choices=AGGREGATOR_PLATFORM_CHOICES,
        default=UNITPAY,
        verbose_name=_('Aggregator')
    )
    trusted_ips_verification = models.BooleanField(
        default=False,
        verbose_name=_('Trusted IPs verification')
    )
    trusted_ips_list = models.ManyToManyField(
        blank=True,
        to='TrustedIP',
        related_name='trusted_ips',
        verbose_name=_('Trusted IPs list')
    )
    public_key = models.CharField(
        max_length=255,
        verbose_name=_('Public key')
    )
    secret_key = models.CharField(
        max_length=255,
        verbose_name=_('Secret key')
    )
    secret_key2 = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_('Second secret key')
    )

    def __str__(self):
        return '{}({})'.format(self.get_platform_display(), self.public_key)


class Payment(models.Model):
    class Meta:
        db_table = 'payment'
        verbose_name = _('Payment')
        verbose_name_plural = _('Payments')

    number = models.ImageField(
        null=True,
        verbose_name=_('Number')
    )
    status = models.BooleanField(
        default=False,
        verbose_name=_('Status')
    )
    aggregator = models.ForeignKey(
        to='Aggregator',
        on_delete=models.CASCADE,
        verbose_name=_('Aggregator')
    )
    cart = models.ForeignKey(
        to=Cart,
        on_delete=models.CASCADE,
        verbose_name=_('Cart')
    )
    created_date = models.DateTimeField(
        default=timezone.now,
        verbose_name=_('Created date')
    )
    completed_date = models.DateTimeField(
        verbose_name=_('Completed date')
    )
