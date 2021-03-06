# Generated by Django 2.2.4 on 2019-08-18 17:03

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='picture',
            field=models.ImageField(blank=True, upload_to=accounts.models.user_filename),
        ),
        migrations.AddField(
            model_name='userrequest',
            name='token',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='userrequest',
            name='uid',
            field=models.CharField(default='', max_length=20),
        ),
    ]
