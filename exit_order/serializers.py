from datetime import datetime

from rest_framework import serializers

from .models import ExitOrder, ExitOrderProduct

from products.serializers import ProductSerializer
from building_work.serializers import BuildingWorkSerializer
from accounts.serializers import UserSerializer

class ExitOrderProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = ExitOrderProduct
		fields = ('id', 'product', 'quantity', 'unit_price', 'price')

	def to_representation(self, instance):
		response = super().to_representation(instance)
		response['product'] = ProductSerializer(instance.product).data
		return response

class ExitOrderSerializer(serializers.ModelSerializer):
	products = ExitOrderProductSerializer(read_only=True, many=True)
	created_by = UserSerializer(required=False)
	
	class Meta:
		model = ExitOrder
		fields = ('id', 'created_date', 'created_by', 'building', 'products')

	def get_validation_exclutions(self):
		exclutions = super(ExitOrderSerializer, self).get_validation_exclutions()
		return exclutions + ['created_by']

	def to_representation(self, instance):
		response = super().to_representation(instance)
		response['building'] = BuildingWorkSerializer(instance.building).data
		return response

	def create(self, validated_data, request=None, products=None):
		print(validated_data)
		order_obj = ExitOrder(
			created_date = datetime.today(),
			building = validated_data.get('building'),
			created_by = validated_data['request'].user
		)

		order_obj.save()

		for prod in validated_data['products']:
			prod_obj = ExitOrderProduct.objects.create(
				product_id=prod['product']['id'],
				quantity=prod['quantity'],
				unit_price=prod['unit_price'],
				price=0.0,
				order=order_obj
			)
			
		return order_obj