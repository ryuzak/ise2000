# Generated by Django 2.2.5 on 2020-03-09 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exit_order', '0007_auto_20200308_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exitorder',
            name='building',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='building_work.BuildingWork'),
        ),
    ]
