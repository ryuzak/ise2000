# Generated by Django 2.2.5 on 2020-03-09 03:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order', '0011_auto_20200308_0455'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
