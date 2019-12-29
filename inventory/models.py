from django.db import models
from django.utils import timezone
from PIL import Image
from django.core.validators import int_list_validator
 

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
    image = models.ImageField(default="default2.jpg", upload_to='item_pics')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Item, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
            


class Orders(models.Model):
    custId = models.CharField(max_length=10)
    contact = models.IntegerField(max_length=10)
    amount = models.FloatField(max_length=10)
    productsId = models.CharField(validators=[int_list_validator], max_length=100)
    Address = models.CharField(max_length=200)
    dagent = models.IntegerField(max_length=10)
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.custId
 


