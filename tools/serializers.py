from rest_framework import serializers

from tool_category.serializers import ToolCategorySerializer
from .models import Tool

class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ['id', 'name', 'code', 'description', 'measure', 'category', 'status']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['category'] = ToolCategorySerializer(instance.category).data
        return response

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.code = validated_data.get('code', instance.code)
        instance.description = validated_data.get('description', instance.description)
        instance.measure = validated_data.get('measure', instance.measure)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance