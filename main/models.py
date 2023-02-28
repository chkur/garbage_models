from django.db import models
from django.utils import timezone

from .managers import GarbageManager


class GarbageModel(models.Model):
    objects = GarbageManager()

    class Meta:
        abstract = True

    def save(
        self,
        force_insert=False,
        force_update=False,
        using="garbage",
        update_fields=None,
    ):
        return super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )

    def delete(self, using="garbage", keep_parents=False):
        return super().delete(
            using,
            keep_parents,
        )


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


class Selling(GarbageModel):
    product = models.ForeignKey(
        "Product",
        db_index=True,
        db_constraint=False,
        on_delete=models.DO_NOTHING,
    )
    dt = models.DateTimeField(
        default=timezone.now,
    )
    quantity = models.IntegerField(
        default=1,
    )
    order_data = models.JSONField(
        default=dict,
    )
