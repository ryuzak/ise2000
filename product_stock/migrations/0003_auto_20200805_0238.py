# Generated by Django 2.2.5 on 2020-08-05 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_stock', '0002_productstock_min_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='productstock',
            name='credit_price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='productstock',
            name='sale_price',
            field=models.FloatField(default=0.0),
        ),
    ]
