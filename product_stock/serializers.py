from rest_framework import serializers

from .models import ProductStock
from products.serializers import ProductSerializer

class ProductStockSerializer(serializers.ModelSerializer):
    updated_date = serializers.ReadOnlyField()

    class Meta:
        model = ProductStock
        fields = ('id', 'product','unit_price', 'price', 'stock', 'updated_date')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['product'] = ProductSerializer(instance.product).data
        return response
