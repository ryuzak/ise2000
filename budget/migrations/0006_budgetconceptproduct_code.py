# Generated by Django 2.2.5 on 2020-07-04 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0005_budget_final_price_subtotal'),
    ]

    operations = [
        migrations.AddField(
            model_name='budgetconceptproduct',
            name='code',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
    ]
