from datetime import datetime

from django.db import models


from building_work.models import BuildingWork
from accounts.models import User
from products.models import Product
# Create your models here.
class PurchaseOrder(models.Model):
    purchase_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(default=datetime.now, blank=True)
    buiilding = models.ForeignKey(BuildingWork, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    deliver_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='deliver_to')
    provider_name = models.CharField(max_length=100)
    provider_addres = models.CharField(max_length=250)
    provider_phone = models.CharField(max_length=10)
    total_price = models.FloatField(default=0.0)
    note = models.CharField(max_length=500)

    class Meta:
    	db_table = 'purchase_order'

class PruchaseOrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0)
    unit_price = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
    order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)

    class Meta:
    	db_table = 'pruchase_order_products'