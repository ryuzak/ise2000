# Generated by Django 2.2.5 on 2019-10-14 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_picture'),
        ('purchase_order', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PruchaseOrderProduct',
            new_name='PurchaseOrderProduct',
        ),
        migrations.RenameField(
            model_name='purchaseorder',
            old_name='buiilding',
            new_name='building',
        ),
    ]