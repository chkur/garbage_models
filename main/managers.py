from django.db import models


class GarbageManager(models.Manager):
    def get_queryset(self):
        return models.QuerySet(self.model, using="garbage")
