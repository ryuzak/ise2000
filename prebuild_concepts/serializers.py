from rest_framework import serializers

from .models import PrebuildBudgetConcept, PrebuildBudgetProducts

from product_stock.serializers import ProductStockSerializer

class PrebuildBudetProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrebuildBudgetProducts
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['product'] = ProductStockSerializer(instance.product).data
        return response

class PrebuildBudgetConceptSerializer(serializers.ModelSerializer):
    PrebuildBudetProducts = PrebuildBudetProductsSerializer(many=True, read_only=True)
    
    class Meta:
        model = PrebuildBudgetConcept
        fields = ('id', 'name', 'code', 'PrebuildBudetProducts',)

    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['products'] = 

    


    

