import uuid

from django.db import models

from django.utils.translation import gettext as _


class Coupon(models.Model):
    class Meta:
        db_table = 'coupon'
        verbose_name = _('Coupon')
        verbose_name_plural = _('Coupons')

    VALUE = 'VL'
    PERCENT = 'PR'
    ITEM = 'ITM'

    COUPON_TYPE_CHOICES = (
        (VALUE, _('Monetary')),
        (PERCENT, _('Percent')),
        (ITEM, _('Gift')),
    )

    coupon = models.CharField(
        max_length=255,
        default=uuid.uuid4,
        verbose_name=_('Coupon')
    )
    type = models.CharField(
        max_length=3,
        choices=COUPON_TYPE_CHOICES,
        default=VALUE,
        verbose_name=_('Coupon type')
    )
    value = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name=_('Discount value')
    )
    percent = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name=_('Discount percent')
    )
    items = models.ManyToManyField(
        to='Item',
        blank=True,
        verbose_name=_('Coupon items')
    )
    count = models.IntegerField(
        blank=True,
        null=True,
        default=None,
        verbose_name=_('Count')
    )

    def __str__(self):
        return '{}'.format(self.type)
