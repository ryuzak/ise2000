# Generated by Django 2.2.3 on 2019-07-29 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building_work', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildingwork',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
