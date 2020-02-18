from django.db import models

from building_work.models import BuildingWork
from accounts.models import User
from product_stock.models import ProductStock

# Create your models here.

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    building = models.ForeignKey(BuildingWork, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    product_cost_subtotal = models.FloatField(default=0.0)
    work_price_subtotal = models.FloatField(default=0.0)
    sale_price_subtotal = models.FloatField(default=0.0)

    class Meta:
        db_table = 'budgets'

class BudgetProducts(models.Model):
    product = models.ForeignKey(ProductStock, on_delete=models.CASCADE, null=True)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, null=True)
    quantity = models.FloatField(default=0.0)
    product_unit_cost = models.FloatField(default=0.0)
    product_cost = models.FloatField(default=0.0)
    work_unit_price = models.FloatField(default=0.0)
    work_price = models.FloatField(default=0.0)
    sale_unit_price = models.FloatField(default=0.0)
    sale_price = models.FloatField(default=0.0)

    class Meta:
        db_table = 'budget_products'
