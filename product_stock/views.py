from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from django.shortcuts import get_object_or_404

from .serializers import ProductStockSerializer
from .models import ProductStock

class RetrieveProductStockAPIView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self,request):
		stock = ProductStock.objects.filter(product__status=True)
		serializer = ProductStockSerializer(stock, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)