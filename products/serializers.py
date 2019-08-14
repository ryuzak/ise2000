from rest_framework import serializers

from product_category.serializers import ProductCategorySerializer
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'code', 'description', 'measure', 'category', 'status']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['category'] = ProductCategorySerializer(instance.category).data
        return response

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.measure = validated_data.get('measure', instance.measure)
    #     instance.category = validated_data.get('category_id', instance.category)
    #     instance.save()
    #     print(instance.__dict__)
    #     return instance