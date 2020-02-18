from django.db import models

# Create your models here.
class Provider(models.Model):
	name = models.CharField(max_length=100, verbose_name='Nombre')
	address = models.CharField(max_length=256, verbose_name='Dirección')
	phone = models.CharField(max_length=10, verbose_name='Telefono')
	contact_name = models.CharField(max_length=100, verbose_name='Nombre contacto')
	contact_phone = models.CharField(max_length=10, verbose_name='Telefono contacto')
	status = models.BooleanField(default=True, verbose_name='Status')

	class Meta:
		db_table='providers'