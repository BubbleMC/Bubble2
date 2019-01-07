from django.db import models

from django.template.defaultfilters import slugify
from django.utils.translation import gettext as _


class Category(models.Model):
    class Meta:
        db_table = 'category'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    name = models.CharField(
        max_length=255,
        verbose_name=_('Name')
    )
    slug = models.SlugField(
        unique=True,
        max_length=255,
        verbose_name=_('Slug')
    )
    icon = models.ImageField(
        blank=True,
        upload_to='categories/',
        verbose_name=_('Preview image')
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save()

    def __str__(self):
        return '{}'.format(self.name)
