from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from django.shortcuts import get_object_or_404

from .serializers import ToolSerializer
from .models import Tool

class CreateToolAPIView(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self, request):
		tool_obj = request.data
		print(tool_obj)
		serializer = ToolSerializer(data=tool_obj)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

class RetrieveToolsAPIView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request):
		tools = Tool.objects.filter(status=True)
		serializer = ToolSerializer(tools, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

class RetrieveUpdateDeleteToolAPIView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request, tool_id):
		tool_obj = get_object_or_404(Tool, pk=tool_id)
		serializer = ToolSerializer(tool_obj)
		print(serializer.data)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def put(self, request, tool_id):
		tool_obj = get_object_or_404(Tool, pk=tool_id)
		serializer_data = request.data.get('tool',{})
		serializer = ToolSerializer(instance=tool_obj, data=serializer_data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_200_OK)

	def delete(self, request, tool_id):
		tool_obj = Tool.objects.get(pk=tool_id)
		tool_obj.status = False
		tool_obj.save()
		serializer = ToolSerializer(tool_obj)
		return Response(status=status.HTTP_200_OK)

class RetrieveToolNameListAPIView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request, tool_name):
		tool_obj = Tool.objects.filter(name__icontains=tool_name)
		serializer = ToolSerializer(tool_obj, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)