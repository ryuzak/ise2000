# Generated by Django 2.2.3 on 2019-07-29 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuildingWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=150)),
                ('contact_name', models.CharField(max_length=150)),
                ('project_name', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=150)),
                ('contact_mail', models.CharField(max_length=100)),
                ('contact_phone', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'building_work',
            },
        ),
    ]
