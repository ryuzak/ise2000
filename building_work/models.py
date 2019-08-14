from django.db import models

# Create your models here.
class BuildingWork(models.Model):
	client_name = models.CharField(max_length=150)
	contact_name = models.CharField(max_length=150)
	project_name = models.CharField(max_length=150)
	location = models.CharField(max_length=150)
	contact_mail = models.CharField(max_length=100)
	contact_phone = models.CharField(max_length=10)
	status = models.BooleanField(default=True)

	class Meta:
		db_table = 'building_work'