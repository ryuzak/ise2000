from django.db import models

# Create your models here.
class ProductCategory(models.Model):
	name = models.CharField(max_length=75)
	description = models.CharField(max_length=300)
	status = models.BooleanField(default=True)

	class Meta:
		db_table = 'product_category'