from django import forms

from django.utils.translation import gettext_lazy as _

from shop.models import category, coupon, item


class CouponForm(forms.ModelForm):
    class Meta:
        model = coupon.Coupon
        exclude = []

    def clean(self):
        coupon_type = self.cleaned_data.get('type')

        value = self.cleaned_data.get('value')
        percent = self.cleaned_data.get('percent')
        items = self.cleaned_data.get('items')

        if coupon_type == coupon.Coupon.VALUE and not value:
            raise forms.ValidationError(_('Value cannot be empty with monetary type'))
        elif coupon_type == coupon.Coupon.PERCENT and not percent:
            raise forms.ValidationError(_('Percent cannot be empty with percent type'))
        elif coupon_type == coupon.Coupon.ITEM and not items:
            raise forms.ValidationError(_('Items cannot be empty with gift type'))

        return self.cleaned_data


class CategoryForm(forms.ModelForm):
    class Meta:
        model = category.Category
        exclude = ['slug']


class ItemForm(forms.ModelForm):
    class Meta:
        model = item.Item
        exclude = ['slug']
