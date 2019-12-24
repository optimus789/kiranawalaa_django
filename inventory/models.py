from django.db import models
from django.utils import timezone

# Create your models here.
"""TAX= (
    ('0.0', 'No tax'),
    ('8.0', "7 % gst"),
    ('12.0', '12 % gst'),
    ('18.0', '18 % gst')
    )

CAT = (
    ('fruit', 'Fruit'),
    ('beverage', "Beverage"),
    ('biscuit', 'Biscuits'),
    ('grains', 'Grains'),
    ('vegetables', 'Vegetables')
)

UNITS = (
    ('kg', 'KiloGram(KG)'),
    ('lt', "Litre(LT)"),
    ('gm', 'Gram(gm)'),
    ('ml', 'MiliLitre(ml)'),
    ('Nos', 'Number of pieces')
)"""


class Item(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    category = models.CharField(max_length=40)
    cprice = models.FloatField()
    sprice = models.FloatField()
    mrp = models.FloatField()
    tax = models.FloatField(default=0.00)
    stock = models.PositiveIntegerField()
    units = models.CharField(max_length=10)
    image = models.ImageField(default="default.jpg", upload_to='item_pics')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title