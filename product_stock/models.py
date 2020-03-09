from django.db import models

from products.models import Product
# Create your models here.

class ProductStock(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
	unit_price = models.FloatField(default=0.0)
	price = models.FloatField(default=0.0)
	stock = models.FloatField(default=0.0)
	updated_date = models.DateTimeField(auto_now_add=True)
	min_stock = models.FloatField(default=0.0)

	class Meta:
		db_table = 'product_stock'


