from django.contrib import admin
from django.urls import reverse

from payments.forms import AggregatorForm
from payments import models

from django.utils.translation import gettext as _


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('cart', 'cart_owner', 'status', 'payment')

    def cart_owner(self, obj):
        return obj.cart.username

    cart_owner.short_description = 'Cart owner'


@admin.register(models.TrustedIP)
class TrustedServerAdmin(admin.ModelAdmin):
    search_fields = ['ip']


@admin.register(models.Aggregator)
class AggregatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'platform', 'public_key', 'handler_url')
    form = AggregatorForm
    autocomplete_fields = ['trusted_ips_list']

    def handler_url(self, obj):
        return reverse('payment_handler', args=(obj.platform, obj.id))

    handler_url.short_description = _('Link to payment handler')


@admin.register(models.Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass

