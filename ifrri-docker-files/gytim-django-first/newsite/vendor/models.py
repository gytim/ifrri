from django.db import models
from django.conf import settings
from django.utils import timezone


class Vendor(models.Model):
    name = models.CharField(max_length=120)
    country = models.CharField(max_length=3)
    kind = models.CharField(max_length=20)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
