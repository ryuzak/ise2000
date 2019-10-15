from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from django.shortcuts import get_object_or_404

from .serializers import ProductStockSerializer
from .models import ProductStock
from products.models import Product
from products.serializers import ProductSerializer

class RetrieveProductStockAPIView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self,request):
		stock = ProductStock.objects.filter(product__status=True)
		serializer = ProductStockSerializer(stock, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

class CreateProductStockInitialAPIView(APIView):
	permission_classes = (IsAuthenticated, )

	def post(self, request):
		prod_stock = request.data
		prod_id = prod_stock['product']['id']
		del prod_stock['product']
		prod_stock['product'] = prod_id
		print(prod_stock)
		serializer = ProductStockSerializer(data=prod_stock)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

class RetrieveRegisterProductCodeAPIView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request, prod_code):
		try:
			prod_obj = Product.objects.get(code=prod_code)
			serializer = ProductSerializer(prod_obj)
		except Product.DoesNotExist:
			return Response({'message':'El producto no ha sido registrado'}, status=status.HTTP_404_NOT_FOUND)

		try:
			prod_stock = ProductStock.objects.get(product__pk=prod_obj.id)
			return Response({'message':'El producto ya se encuentra en stock'}, status=status.HTTP_400_BAD_REQUEST)
		except ProductStock.DoesNotExist:
			pass

		return Response(serializer.data, status=status.HTTP_200_OK)


class RetrieveProductCodeAPIView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request, prod_code):
		try:
			prod_stock = ProductStock.objects.get(product__code=prod_code)
			serializer = ProductStockSerializer(prod_stock)
		except Product.DoesNotExist:
			return Response({'message':'El producto no ha sido registrado'}, status=status.HTTP_404_NOT_FOUND)

		return Response(serializer.data, status=status.HTTP_200_OK)