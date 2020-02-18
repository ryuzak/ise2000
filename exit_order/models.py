from datetime import datetime

from django.db import models

from products.models import Product
from building_work.models import BuildingWork
from accounts.models import User
# Create your models here.

class ExitOrder(models.Model):
    created_date = models.DateTimeField(default=datetime.today, blank=True)
    building = models.ForeignKey(BuildingWork, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    

    class Meta:
    	db_table = 'exit_order'


class ExitOrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0)
    unit_price = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
    order = models.ForeignKey(ExitOrder, on_delete=models.CASCADE)

    class Meta:
    	db_table = 'exit_order_products'