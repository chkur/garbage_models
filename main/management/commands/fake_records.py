import random

from django.core.management import BaseCommand

from main.models import Category, Product, Selling


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        cat1, _ = Category.objects.get_or_create(name="Common")
        cat2, _ = Category.objects.get_or_create(name="Custom")
        for i in range(1, 1001):
            product = Product.objects.create(
                category=random.choice([cat1, cat2]),
                price=random.choice([100, 1000, 2000, 500]),
                name=f"Product #{i}",
            )
            print(f"\rCreated new product '{product}', {i} of 1000", end="")
            for sell_num in range(random.randint(1, 10)):
                Selling.objects.create(
                    product=product,
                    quantity=random.randint(1, 5),
                    order_data={
                        "customer": f"Customer {sell_num}",
                        "paid": random.choice(["CARD", "CASH "]),
                    },
                )

        Selling.objects.all().update(dt="2020-01-01 00:00+00")
