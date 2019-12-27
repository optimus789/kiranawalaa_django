from django.db import models
from PIL import Image


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    image = models.ImageField(default="default_cust.jpg", upload_to='cust_pics')
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Customer, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



class Deliveryguy(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    image = models.ImageField(default="default_dlvr.jpg", upload_to='delvrygy_pics')
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    drvlicence = models.ImageField(default="licence.jpg", upload_to='delvrygy_pics/docs')
    docname = models.CharField(max_length=50)
    verfdoc = models.ImageField(default="doc.jpg", upload_to="dlvrygy_pics/docs")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Deliveryguy, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        drvlc = Image.open(self.drvlicence.path)
        verfdoc = Image.open(self.verfdoc.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

        if drvlc.height > 300 or drvlc.width > 300:
            output_size = (300, 300)
            drvlc.thumbnail(output_size)
            drvlc.save(self.image.path)

        if verfdoc.height > 300 or verfdoc.width > 300:
            output_size = (300, 300)
            verfdoc.thumbnail(output_size)
            verfdoc.save(self.image.path)
