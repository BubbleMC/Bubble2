from django.contrib import admin

from payments.forms import AggregatorForm
from payments import models


class TrustedServerAdmin(admin.ModelAdmin):
    search_fields = ['ip']


class AggregatorAdmin(admin.ModelAdmin):

    form = AggregatorForm
    autocomplete_fields = ['trusted_ips_list']


class PaymentAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.TrustedIP, TrustedServerAdmin)
admin.site.register(models.Aggregator, AggregatorAdmin)
admin.site.register(models.Payment, PaymentAdmin)
