from rest_framework import serializers

from tool_category.serializers import ToolCategorySerializer
from .models import Tool

class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ['id', 'name', 'model', 'brand', 'serial_number', 'category', 'status']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['category'] = ToolCategorySerializer(instance.category).data
        return response

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.model = validated_data.get('model', instance.model)
        instance.brand = validated_data.get('brand', instance.brand)
        instance.serial_number = validated_data.get('serial_number', instance.serial_number)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance