from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from django.shortcuts import get_object_or_404

from .serializers import ProductSerializer
from .models import Product

class CreateProductAPIView(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self, request):
		product_obj = request.data
		serializer = ProductSerializer(data=product_obj)
		serializer.is_valid(raise_exception=True)
		print(f'serializer is {serializer}')
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

class RetrieveProductsAPIView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request):
		prods = Product.objects.filter(status=True)
		serializer = ProductSerializer(prods, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

class RetrieveUpdateDeleteProductAPIView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request, prod_id):
		prod_obj = get_object_or_404(Product, pk=prod_id)
		serializer = ProductSerializer(prod_obj)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def put(self, request, prod_id):
		prod_obj = get_object_or_404(Product, pk=prod_id)
		serializer_data = request.data.get('product',{})
		serializer = ProductSerializer(instance=prod_obj, data=serializer_data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		print(serializer.data)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def delete(self, request, prod_id):
		prod_obj = Product.objects.get(pk=prod_id)
		prod_obj.status = False
		prod_obj.save()
		serializer = ProductSerializer(prod_obj)
		return Response(serializer.data, status=status.HTTP_200_OK)