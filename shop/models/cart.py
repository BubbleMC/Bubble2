from django.db import models

from django.utils.translation import gettext as _


class Cart(models.Model):
    class Meta:
        db_table = 'cart'
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')

    session = models.CharField(
        max_length=255,
        verbose_name=_('Owner`s session')
    )
    username = models.CharField(
        max_length=255,
        verbose_name=_('Owner`s nickname')
    )
    items = models.ManyToManyField(
        to='Item',
        verbose_name=_('Cart items')
    )

    @property
    def price(self):
        return sum([item.price for item in self.items.all()])

    def __str__(self):
        return '{}({}) Price: {}'.format(self.username, self.items.count(), self.price)
