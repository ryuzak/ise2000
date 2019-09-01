from django.db import models

from building_work.models import BuildingWork
from accounts.models import User
from tools.models import Tool
# Create your models here.
class ToolLend(models.Model):
	lend_date = models.DateField(auto_now_add=True)
	building = models.ForeignKey(BuildingWork, on_delete=models.CASCADE, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	return_date = models.DateField(blank=True, null=True)
	notes = models.CharField(max_length=300, null=True)

	class Meta:
		db_table = 'tools_lend'


class ToolLendbridge(models.Model):
	tool = models.ForeignKey(Tool, on_delete=models.CASCADE, null=True)
	lend = models.ForeignKey(ToolLend, on_delete=models.CASCADE, null=True)
	quantity = models.FloatField(default=0.0)

	class Meta:
		db_table = 'tool_lend_quantity'