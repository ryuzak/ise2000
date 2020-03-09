from rest_framework import serializers

from .models import Budget, BudgetProducts
from product_stock.models import ProductStock

from accounts.serializers import UserSerializer
from building_work.serializers import BuildingWorkSerializer
from product_stock.serializers import ProductStockSerializer

class BudgetProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetProducts
        fields = ('id', 'product', 'budget', 'quantity', 'product_unit_cost', 'product_cost', 'work_unit_price', 'work_price', 'sale_unit_price', 'sale_price',)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['product'] = ProductStockSerializer(instance.product).data
        #responser['budget'] = BudgetSerializer(instance.budget).data
        return response

class BudgetSerializer(serializers.ModelSerializer):
    products = BudgetProductSerializer(read_only=True, many=True)
    class Meta:
        model = Budget
        fields = ('id', 'user', 'building', 'products', 'created_date', 'product_cost_subtotal', 'work_price_subtotal', 'sale_price_subtotal', 'actual_budget_subtotal',)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = UserSerializer(instance.user).data
        response['building'] = BuildingWorkSerializer(instance.building).data
        response['products'] = BudgetProductSerializer(instance.budgetproducts_set.all(), many=True).data
        return response

    """ def create(self, validated_data):
        budget = Budget.objects.create(**validated_data)
        return budget """

