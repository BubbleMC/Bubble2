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
        to="Item",
        verbose_name=_('Cart items')
    )

    def __str__(self):
        return "Cart: {}, items count: {}".format(self.username, self.items.count())
