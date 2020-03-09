from datetime import datetime

from django.db import models

from building_work.models import BuildingWork
from accounts.models import User
from products.models import Product
from provider.models import Provider
# Create your models here.
class PurchaseOrder(models.Model):
    purchase_date = models.DateTimeField(default=datetime.today, blank=True)
    delivery_date = models.DateTimeField(default=datetime.today, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    building = models.ForeignKey(BuildingWork, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    deliver_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='deliver_to')
    total_price = models.FloatField(default=0.0)
    note = models.CharField(max_length=500)
    status = models.BooleanField(default=False)
    order_pdf = models.CharField(max_length=512, null=True)

    class Meta:
    	db_table = 'purchase_order'

class PurchaseOrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0)
    unit_price = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
    order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True)
    delivered = models.BooleanField(default=False, null=True)
    status = models.BooleanField(default=False)

    class Meta:
    	db_table = 'pruchase_order_products'