# Generated by Django 2.2.5 on 2020-03-08 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exit_order', '0006_exitorder_order_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exitorder',
            name='order_pdf',
            field=models.CharField(max_length=512, null=True),
        ),
    ]
