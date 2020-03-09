from datetime import datetime

from django.template.loader import render_to_string

from weasyprint import HTML

from rest_framework import serializers

from .models import ExitOrder, ExitOrderProduct
from budget.models import Budget
from accounts.models import User

from products.serializers import ProductSerializer
from building_work.serializers import BuildingWorkSerializer
from accounts.serializers import UserSerializer

class ExitOrderProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = ExitOrderProduct
		fields = ('id', 'product', 'quantity', 'unit_price', 'price', 'status', 'parcial', 'parcial_quantity', 'parcial_left',)

	def to_representation(self, instance):
		response = super().to_representation(instance)
		response['product'] = ProductSerializer(instance.product).data
		return response

class ExitOrderSerializer(serializers.ModelSerializer):
	products = ExitOrderProductSerializer(many=True, read_only=True)
	created_by = UserSerializer(required=False)
	
	class Meta:
		model = ExitOrder
		fields = ('id', 'created_date', 'created_by', 'building', 'products', 'total', 'status', 'order_pdf', 'parcial', )

	def get_validation_exclutions(self):
		exclutions = super(ExitOrderSerializer, self).get_validation_exclutions()
		return exclutions + ['created_by']

	def to_representation(self, instance):
		response = super().to_representation(instance)
		response['building'] = BuildingWorkSerializer(instance.building).data
		return response

	def create(self, validated_data, request=None, products=None):
		building = validated_data.get('building', None)
		order_obj = ExitOrder(
			created_date = validated_data.get('created_date', datetime.today),
			building = validated_data.get('building', None),
			created_by = validated_data['request'].user,
			total = validated_data.get('total', 0.0)
		)
		if building:
			budget_obj = Budget.objects.get(building__pk=building.id)
			budget_obj.actual_budget_subtotal += order_obj.total
			budget_obj.save()

		order_obj.save()
		prod_list = []
		for prod in validated_data['products']:
			prod_obj = ExitOrderProduct.objects.create(
				product_id=prod['product']['id'],
				quantity=prod['quantity'],
				unit_price=prod['unit_price'],
				price=prod['total'],
				parcial_left=prod['quantity'],
				order=order_obj
			)
			prod_list.append(prod_obj)
		context = {}
		context['order'] = order_obj
		context['product_list'] = prod_list
		context['user'] = User.objects.get(pk=order_obj.created_by_id)
		file_html = render_to_string('exit_order/exit_order_pdf.html', context)
		file_pdf = HTML(string=file_html).write_pdf()
		with open(f'media/orders/exit/pdf/{order_obj.id}.pdf', 'wb') as f:
			f.write(file_pdf)
		
		order_obj.order_pdf = f'media/orders/exit/pdf/{order_obj.id}.pdf'
		order_obj.save()

		return order_obj