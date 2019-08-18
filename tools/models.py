from django.db import models

from tool_category.models import ToolCategory
# Create your models here.
def tool_image(self, filename):
    url = "tool_images/%s/%s" % (self.id, filename)
    return url

class Tool(models.Model):
	name = models.CharField(max_length=75)
	model = models.CharField(max_length=75)
	brand = models.CharField(max_length=100)
	serial_number = models.IntegerField(default=0)
	status = models.BooleanField(default=True)
	category = models.ForeignKey(ToolCategory, on_delete=models.CASCADE)
	picture = models.ImageField(upload_to=tool_image, blank=True)

	class Meta:
		db_table = 'tools'