from django.db import models

# Create your models here.
class Provider(models.Model):
	name = models.CharField(max_length=100, verbose_name='Nombre')
	address = models.CharField(max_length=256, verbose_name='Dirección')
	phone = models.CharField(max_length=10, verbose_name='Telefono')
	contact_name = models.CharField(max_length=100, verbose_name='Nombre contacto')
	contact_phone = models.CharField(max_length=10, verbose_name='Telefono contacto')
	contact_email = models.CharField(max_length=256, verbose_name='Correo proveedor')
	status = models.BooleanField(default=True, verbose_name='Status')
	category = models.CharField(max_length=30, verbose_name='Categoria')

	class Meta:
		db_table='providers'