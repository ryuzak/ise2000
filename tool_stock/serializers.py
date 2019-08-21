from rest_framework import serializers

from .models import ToolStock
from tools.serializers import ToolSerializer

class ToolStockSerializer(serializers.ModelSerializer):
    updated_date = serializers.ReadOnlyField()

    class Meta:
        model = ToolStock
        fields = ('id', 'tool','unit_price', 'price', 'stock', 'updated_date')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['tool'] = ToolSerializer(instance.tool).data
        return response
