from rest_framework import serializers
from .models import ToolCategory

class ToolCategorySerializer(serializers.ModelSerializer):

	class Meta(object):
		model = ToolCategory
		fields = ('id', 'name', 'description','status')

	def update(self, instance, validated_data):
		instance.name = validated_data.get('name', instance.name)
		instance.description = validated_data.get('description', instance.description)
		instance.save()
		return instance