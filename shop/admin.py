from django.contrib import admin

from shop.forms import CategoryForm, CouponForm, ItemForm
from shop.models import category, cart, coupon, item


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm


class CartAdmin(admin.ModelAdmin):
    pass


class CouponAdmin(admin.ModelAdmin):
    form = CouponForm


class ItemAdmin(admin.ModelAdmin):
    form = ItemForm


admin.site.register(category.Category, CategoryAdmin)
admin.site.register(cart.Cart, CartAdmin)
admin.site.register(coupon.Coupon, CouponAdmin)
admin.site.register(item.Item, ItemAdmin)
