from django.db import models

from django.template.defaultfilters import slugify
from django.utils.translation import gettext as _


class Item(models.Model):
    class Meta:
        db_table = 'item'
        verbose_name = _('Item')
        verbose_name_plural = _('Items')

    name = models.CharField(
        max_length=255,
        verbose_name=_('Name')
    )
    slug = models.SlugField(
        unique=True,
        max_length=255,
        verbose_name=_('Slug')
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        verbose_name=_('Category')
    )
    icon = models.ImageField(
        blank=True,
        upload_to='items/',
        verbose_name=_('Preview image')
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name=_('Price')
    )
    count = models.IntegerField(
        blank=True,
        null=True,
        default=None,
        verbose_name=_('Count')
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Item, self).save()

    def __str__(self):
        return '{}'.format(self.name)
