from uuid import uuid4

from django.test import TestCase

from shop.tests.factories import ItemFactory
from shop.forms import CouponForm
from shop.models import coupon


class ModelsTestCase(TestCase):
    value = 20.3
    percent = 2.33

    def setUp(self):
        self.item = ItemFactory()

    def test_value_type_without_value(self):
        form = CouponForm({
            'coupon': uuid4(),
            'type': coupon.Coupon.VALUE,
        })

        self.assertFalse(form.is_valid())

    def test_value_type_with_value(self):
        form = CouponForm({
            'coupon': uuid4(),
            'type': coupon.Coupon.VALUE,
            'value': self.value,
        })

        self.assertTrue(form.is_valid())

    def test_percent_type_without_percent(self):
        form = CouponForm({
            'coupon': uuid4(),
            'type': coupon.Coupon.PERCENT,
        })

        self.assertFalse(form.is_valid())

    def test_percent_type_with_percent(self):
        form = CouponForm({
            'coupon': uuid4(),
            'type': coupon.Coupon.PERCENT,
            'percent': self.percent,
        })

        self.assertTrue(form.is_valid())

    def test_item_type_without_items(self):
        form = CouponForm({
            'coupon': uuid4(),
            'type': coupon.Coupon.ITEM,
        })

        self.assertFalse(form.is_valid())

    def test_item_type_with_items(self):
        form = CouponForm({
            'coupon': uuid4(),
            'type': coupon.Coupon.ITEM,
            'items': [self.item],
        })

        self.assertTrue(form.is_valid())
