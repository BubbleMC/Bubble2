from django import forms

from django.utils.translation import gettext_lazy as _

from payments import models


class AggregatorForm(forms.ModelForm):
    class Meta:
        model = models.Aggregator
        exclude = []

    def clean(self):
        trusted_ips_verification = self.cleaned_data.get('trusted_ips_verification')
        trusted_ips_list = self.cleaned_data.get('trusted_ips_list')
        if trusted_ips_verification and not trusted_ips_list:
            raise forms.ValidationError(_('You can not enable trusted verification without adding any IP...'))

        return self.cleaned_data
