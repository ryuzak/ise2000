from datetime import datetime

from django.template.loader import render_to_string

from weasyprint import HTML

from rest_framework import serializers

from .models import PurchaseOrderProduct, PurchaseOrder
from products.models import Product
from accounts.models import User

from products.serializers import ProductSerializer
from building_work.serializers import BuildingWorkSerializer
from accounts.serializers import UserSerializer
from provider.serializers import ProviderSerializer

class PurchaseOrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderProduct
        fields = ('id', 'product', 'quantity', 'unit_price', 'price', 'order', 'provider', 'status',)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['product'] = ProductSerializer(instance.product).data
        response['provider'] = ProviderSerializer(instance.provider).data
        return response

class PurchaseOrderSerializer(serializers.ModelSerializer):
    products = PurchaseOrderProductSerializer(read_only=True, many=True)
    note = serializers.CharField(required=False)
    #building = BuildingWorkSerializer(required=False)
    #created_by = UserSerializer(required=False)

    class Meta:
        model = PurchaseOrder
        fields = ('id', 'products', 'purchase_date', 'delivery_date', 'building', 'created_by', 'deliver_to', 'total_price', 'note', 'status', 'order_pdf',)

    def get_validation_exclutions(self):
        exclutions = super(ExitOrderSerializer, self).get_validation_exclutions()
        return exclutions + ['note', 'building']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['created_by'] = UserSerializer(instance.created_by).data
        response['deliver_to'] = UserSerializer(instance.deliver_to).data
        return response

    def create(self, validated_data, products=None):
        order_obj = PurchaseOrder(
            delivery_date = validated_data.get('delivery_date', '1970-01-01T00:00:00'),
            building = validated_data.get('building', None),
            created_by = validated_data.get('created_by', None),
            deliver_to = validated_data.get('deliver_to', None),
            total_price = validated_data.get('total_price', 0.00),
            note = validated_data.get('note', '')
        )

        order_obj.save()
        prod_list = []
        for prod in validated_data.get('products', []):
            prod_obj = PurchaseOrderProduct.objects.create(
                product_id=prod['product']['id'],
                quantity=prod['quantity'],
                unit_price=prod['unit_price'],
                price=prod['total'],
                order=order_obj,
                provider_id = prod['provider']
            )
            prod_list.append(prod_obj)

        context = {}
        context['order'] = order_obj
        context['product_list'] = prod_list
        context['user'] = User.objects.get(pk=order_obj.created_by_id)
        file_html = render_to_string('purchase_order/purchase_order_pdf.html', context)
        file_pdf = HTML(string=file_html).write_pdf()
        with open(f'media/orders/purchase/pdf/{order_obj.id}.pdf', 'wb') as f:
            f.write(file_pdf)

        order_obj.order_pdf = f'media/orders/purchase/pdf/{order_obj.id}.pdf'
        order_obj.save()
        return order_obj