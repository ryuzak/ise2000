# Generated by Django 2.2.5 on 2019-10-14 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order', '0003_auto_20191014_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='purchase_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
