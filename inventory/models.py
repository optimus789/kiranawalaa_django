from django.db import models
from django.utils import timezone

# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 1000)
    category = models.CharField(max_length = 40)
    cprice = models.FloatField()
    sprice = models.FloatField()
    mrp = models.FloatField()
    tax = models.FloatField(default = 0.00)
    stock = models.PositiveIntegerField()
    units = models.CharField(max_length = 10)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title