# Generated by Django 3.0.1 on 2019-12-27 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191227_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address_line1',
            field=models.CharField(max_length=255),
        ),
    ]
