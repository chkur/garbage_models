from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100,
    )


class Product(models.Model):
    name = models.CharField(
        max_length=1024,
    )
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.PROTECT,
    )


class Selling(models.Model):
    product = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
    )
    dt = models.DateTimeField(
        auto_now_add=True,
    )
    quantity = models.IntegerField(
        default=1,
    )
    order_data = models.JSONField(
        default=dict,
    )
