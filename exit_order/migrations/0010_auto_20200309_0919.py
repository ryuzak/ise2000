# Generated by Django 2.2.5 on 2020-03-09 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exit_order', '0009_auto_20200309_0653'),
    ]

    operations = [
        migrations.AddField(
            model_name='exitorderproduct',
            name='parcial_left',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='exitorderproduct',
            name='parcial',
            field=models.BooleanField(default=True),
        ),
    ]
