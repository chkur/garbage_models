# Generated by Django 4.1.7 on 2023-02-27 00:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="selling",
            name="order_data",
            field=models.JSONField(default=dict),
        ),
    ]
