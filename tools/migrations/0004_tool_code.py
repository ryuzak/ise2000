# Generated by Django 2.2.5 on 2020-04-23 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0003_auto_20190818_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='code',
            field=models.CharField(default='', max_length=75),
            preserve_default=False,
        ),
    ]
