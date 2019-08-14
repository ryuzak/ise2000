from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from django.shortcuts import get_object_or_404

from .serializers import ProductCategorySerializer
from .models import ProductCategory

class CreateCategoryProductAPIView(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self, request):
		cat_product = request.data
		serializer = ProductCategorySerializer(data=cat_product)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

class RetrieveCategoryProductsAPIView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request):
		cats = ProductCategory.objects.filter(status=True)
		serializer = ProductCategorySerializer(cats, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

class RetrieveUpdateDeleteCategoryProductsAPIView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request, cat_id):
		cat_obj = get_object_or_404(ProductCategory, pk=cat_id)
		serializer = ProductCategorySerializer(cat_obj)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def put(self, request, cat_id):
		cat_obj = get_object_or_404(ProductCategory, pk=cat_id)
		serializer_data = request.data.get('category_prod',{})
		serializer = ProductCategorySerializer(instance=cat_obj, data=serializer_data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_200_OK)

	def delete(self, request, cat_id):
		cat_obj = ProductCategory.objects.get(pk=cat_id)
		cat_obj.status = False
		cat_obj.save()
		serializer = ProductCategorySerializer(cat_obj)
		return Response(status=status.HTTP_200_OK)

	