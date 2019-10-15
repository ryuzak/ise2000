from datetime import datetime

from rest_framework import serializers

from .models import PurchaseOrderProduct, PurchaseOrder
from products.models import Product

from products.serializers import ProductSerializer
from building_work.serializers import BuildingWorkSerializer
from accounts.serializers import UserSerializer

class PurchaseOrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderProduct
        fields = ('id', 'product', 'quantity', 'unit_price', 'price', 'order')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['product'] = ProductSerializer(instance.product).data
        return response

class PurchaseOrderSerializer(serializers.ModelSerializer):
    products = PurchaseOrderProductSerializer(read_only=True, many=True)
    note = serializers.CharField(required=False)
    #created_by = UserSerializer(required=False)

    class Meta:
        model = PurchaseOrder
        fields = ('id', 'products', 'purchase_date', 'delivery_date', 'building', 'created_by', 'deliver_to', 'total_price', 'note', 'provider_name', 'provider_addres', 'provider_phone')

    def get_validation_exclutions(self):
        exclutions = super(ExitOrderSerializer, self).get_validation_exclutions()
        return exclutions + ['note']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['building'] = BuildingWorkSerializer(instance.building).data
        response['created_by'] = UserSerializer(instance.created_by).data
        response['deliver_to'] = UserSerializer(instance.deliver_to).data
        return response

    def create(self, validated_data, products=None):
        print(validated_data.get('products', []))
        order_obj = PurchaseOrder(
            purchase_date = datetime.today(),
            delivery_date = validated_data.get('delivery_date', '1970-01-01T00:00:00'),
            building = validated_data.get('building', None),
            created_by = validated_data.get('created_by', None),
            deliver_to = validated_data.get('deliver_to', None),
            provider_phone = validated_data.get('provider_phone', None),
            provider_addres = validated_data.get('provider_addres', None),
            provider_name = validated_data.get('provider_name', None),
            total_price = validated_data.get('total_price', 0.00),
            note = validated_data.get('note', '')
        )

        order_obj.save()

        for prod in validated_data.get('products', []):
            prod_obj = PurchaseOrderProduct.objects.create(
                product_id=prod['product']['id'],
                quantity=prod['quantity'],
                unit_price=prod['unit_price'],
                price=prod['total'],
                order=order_obj
            )
            
        return order_obj