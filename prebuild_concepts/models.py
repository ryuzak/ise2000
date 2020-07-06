from django.db import models

from product_stock.models import ProductStock

# Create your models here.
class PrebuildBudgetConcept(models.Model):
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=256)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'prebuild_budget_concepts'

class PrebuildBudgetProducts(models.Model):
    product = models.ForeignKey(ProductStock, on_delete=models.CASCADE, null=True)
    concept = models.ForeignKey(PrebuildBudgetConcept, on_delete=models.CASCADE, null=True)
    quantity = models.FloatField(default=0.0)
    product_unit_cost = models.FloatField(default=0.0)
    product_cost = models.FloatField(default=0.0)
    work_unit_price = models.FloatField(default=0.0)
    percentage_work_price = models.FloatField(default=0.0)
    work_price = models.FloatField(default=0.0)
    sale_unit_price = models.FloatField(default=0.0)
    percentage_sale_price = models.FloatField(default=0.0)
    sale_price = models.FloatField(default=0.0)

    class Meta:
        db_table = 'prebuild_budget_products'
