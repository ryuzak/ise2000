# Generated by Django 2.2.4 on 2019-08-22 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('building_work', '0003_auto_20190729_0053'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildingwork',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
