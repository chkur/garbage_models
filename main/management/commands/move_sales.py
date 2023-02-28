from django.core.management import BaseCommand

from main.models import Selling

from django.db import transaction


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with transaction.atomic(using="garbage"):
            if Selling.objects.order_by("id").using("garbage").exists():
                return

            old_records = Selling.objects.order_by("id").using("default")
            new_db_data = []
            dt_items = {}
            for data_default in old_records:
                old_data_item = {
                    k: v
                    for k, v in data_default.__dict__.items()
                    if not k.startswith("_")
                }
                dt_items[old_data_item["id"]] = old_data_item["dt"]
                new_db_data.append(Selling(**old_data_item))

            Selling.objects.bulk_create(new_db_data, batch_size=5000)
