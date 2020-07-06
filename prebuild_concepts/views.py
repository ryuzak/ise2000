from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from django.shortcuts import get_object_or_404

from .models import PrebuildBudgetConcept, PrebuildBudgetProducts

from .serializers import PrebuildBudgetConceptSerializer, PrebuildBudetProductsSerializer


class ConceptListAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        concept_list = PrebuildBudgetConcept.objects.filter(status=True)
        serializer = PrebuildBudgetConceptSerializer(concept_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ConceptCreateAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        data = request.data
        serializer = PrebuildBudgetConceptSerializer(data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        for product in data['products']:
            product['concept'] = serializer.data['id']
            serializer_product = PrebuildBudetProductsSerializer(data=product, partial=True)
            serializer_product.is_valid(raise_exception=True)
            serializer_product.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ConceptRetrieveUpdateDeleteAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, concept_id):
        concept_obj = get_object_or_404(PrebuildBudgetConcept, pk=concept_id)
        print(concept_obj.__dict__)
        serializer = PrebuildBudgetConceptSerializer(concept_obj)
        #serializer.data['products'] = serializer.instance.prebuildbudgetproducts_set.all()
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, concept_id):
        concept_obj = get_object_or_404(PrebuildBudgetConcept, pk=concept_id)
        data = request.data
        serializer = PrebuildBudgetConceptSerializer(instance=concept_obj, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        instance = serializer.instance
        print(data)
        instance.prebuildbudgetproducts_set.clear()
        for product in data['products']:
            product['concept'] = instance.id
            serializer_prod = PrebuildBudetProductsSerializer(data=product, partial=True)
            serializer_prod.is_valid(raise_exception=True)
            serializer_prod.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, concept_id):
        concept_obj = get_object_or_404(PrebuildBudgetConcept, pk=concept_id)
        concept_obj.status = False
        concept_obj.save()
        return Response({'status':'OK', 'message':'Eliminado con éxito'}, status=status.HTTP_204_NO_CONTENT)

class ConceptProductsRetrieveAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, instance, concept_id):
        products_list = PrebuildBudgetProducts.objects.filter(concept_id=concept_id)
        serializer = PrebuildBudetProductsSerializer(products_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)