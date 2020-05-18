from rest_framework import serializers

from .models import Budget, BudgetProducts, BudgetConceptProduct
from product_stock.models import ProductStock

from accounts.serializers import UserSerializer
from building_work.serializers import BuildingWorkSerializer
from product_stock.serializers import ProductStockSerializer

class BudgetProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetProducts
        fields = (
            'id', 
            'product', 
            'budget', 
            'concept',
            'quantity', 
            'product_unit_cost', 
            'product_cost', 
            'work_unit_price', 
            'work_price', 
            'percentage_work_price',
            'sale_unit_price', 
            'percentage_sale_price',
            'sale_price',
        )

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['product'] = ProductStockSerializer(instance.product).data
        #responser['budget'] = BudgetSerializer(instance.budget).data
        return response

class BudgetConceptProductSerializer(serializers.ModelSerializer):
    products = BudgetProductSerializer(many=True, read_only=True)
    class Meta:
        model = BudgetConceptProduct
        fields = ('id', 'name', 'products', 'budget')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['products'] = BudgetProductSerializer(instance.budgetproducts_set.all(), many=True).data
        return response 

class BudgetSerializer(serializers.ModelSerializer):
    concepts = BudgetConceptProductSerializer(many=True, read_only=True)
    class Meta:
        model = Budget
        fields = (
            'id', 
            'user', 
            'building', 
            'concepts', 
            'created_date', 
            'product_cost_subtotal', 
            'work_price_subtotal', 
            'sale_price_subtotal', 
            'actual_budget_subtotal',
            'final_price_subtotal',
            'global_percentage_product_cost',
            'global_percentage_work_cost',
            )

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = UserSerializer(instance.user).data
        response['building'] = BuildingWorkSerializer(instance.building).data
        response['concepts'] = BudgetConceptProductSerializer(instance.budgetconceptproduct_set.all(), many=True).data
        return response


