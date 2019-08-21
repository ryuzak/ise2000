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
