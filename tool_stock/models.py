from django.db import models

from tools.models import Tool
# Create your models here.

class ToolStock(models.Model):
	tool = models.ForeignKey(Tool, on_delete=models.CASCADE, null=False)
	unit_price = models.FloatField(default=0.0)
	price = models.FloatField(default=0.0)
	stock = models.FloatField(default=0.0)
	updated_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'tool_stock'
