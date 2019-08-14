from django.db import models

from product_category.models import ProductCategory

def product_image(self, filename):
    url = "product_images/%s/%s" % (self.id, filename)
    return url

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=75)
	code = models.CharField(max_length=50)
	description = models.CharField(max_length=300, blank=True)
	measure = models.CharField(max_length=10)
	status = models.BooleanField(default=True)
	category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
	picture = models.ImageField(upload_to=product_image, blank=True)

	class Meta:
		db_table = 'products'