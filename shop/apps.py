from django.apps import AppConfig


class ShopConfig(AppConfig):
    name = 'shop'

    def ready(self):
        from .models import caregory
        from .models import item
        from .models import cart
        from .models import coupon
