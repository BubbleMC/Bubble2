import factory.fuzzy
from factory.django import DjangoModelFactory

from shop.models import item, category, coupon


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = category.Category

    name = factory.fuzzy.FuzzyText(length=5)


class ItemFactory(DjangoModelFactory):
    class Meta:
        model = item.Item

    name = factory.fuzzy.FuzzyText(length=5)
    category = factory.SubFactory(CategoryFactory)
    price = factory.fuzzy.FuzzyDecimal(0)


class CouponFactory(DjangoModelFactory):
    class Meta:
        model = coupon.Coupon

    type = factory.fuzzy.FuzzyChoice(coupon.Coupon.COUPON_TYPE_CHOICES)
    value = factory.fuzzy.FuzzyDecimal(0)
    percent = factory.fuzzy.FuzzyDecimal(0, 100)
    count = factory.fuzzy.FuzzyInteger(0)

    @factory.post_generation
    def items(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for item in extracted:
                self.items.add(item)
