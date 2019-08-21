from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from django.shortcuts import get_object_or_404

from .serializers import ToolStockSerializer
from .models import ToolStock
from tools.models import Tool
from tools.serializers import ToolSerializer

class RetrieveToolStockAPIView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self,request):
		stock = ToolStock.objects.filter(tool__status=True)
		serializer = ToolStockSerializer(stock, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

class CreateToolStockInitialAPIView(APIView):
	permission_classes = (IsAuthenticated, )

	def post(self, request):
		tool_stock = request.data
		tool_id = tool_stock['tool']['id']
		del tool_stock['tool']
		tool_stock['tool'] = tool_id
		serializer = ToolStockSerializer(data=tool_stock)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

class RetrieveToolModelAPIView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request, tool_model):
		try:
			tool_obj = Tool.objects.get(model=tool_model)
			serializer = ToolSerializer(tool_obj)
		except Tool.DoesNotExist:
			return Response({'message':'La herramienta no ha sido registrada'}, status=status.HTTP_404_NOT_FOUND)

		try:
			stock = ToolStock.objects.get(tool__pk=tool_obj.id)
			return Response({'message':'La herramienta ya se encuentra en inventario'}, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			pass

		return Response(serializer.data, status=status.HTTP_200_OK)