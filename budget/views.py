from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from django.shortcuts import get_object_or_404

from .models import Budget, BudgetProducts, BudgetConceptProduct
from .serializers import BudgetSerializer, BudgetProductSerializer, BudgetConceptProductSerializer

class BudgetCreateAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        budget_data = request.data
        budget_data['user'] = request.user.id
        budget_serializer = BudgetSerializer(data=budget_data)
        budget_serializer.is_valid(raise_exception=True)
        budget_serializer.save()
        for concept in budget_data['concepts']:
            concept['budget'] = budget_serializer.data['id']
            concept_serializer = BudgetConceptProductSerializer(data=concept)
            concept_serializer.is_valid(raise_exception=True)
            concept_serializer.save()
            for product in concept['products']:
                product['budget'] = budget_serializer.data['id']
                product['concept'] = concept_serializer.data['id']
                print(product)
                product_serializer = BudgetProductSerializer(data=product)
                product_serializer.is_valid(raise_exception=True)
                product_serializer.save()

        return Response(budget_serializer.data, status=status.HTTP_201_CREATED)

class BudgetDetailAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, budget_id):
        budget_obj = get_object_or_404(Budget, pk=budget_id)
        serializer = BudgetSerializer(instance=budget_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BudgetBuildingDetailAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, building_id):
        print(Budget.objects.filter(building__id=building_id))
        budget_obj = get_object_or_404(Budget, building__id=building_id)
        serializer = BudgetSerializer(instance=budget_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)