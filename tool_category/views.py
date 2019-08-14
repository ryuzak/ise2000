from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from django.shortcuts import get_object_or_404

from .serializers import ToolCategorySerializer
from .models import ToolCategory

class CreateCategoryToolsAPIView(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self, request):
		cat_product = request.data
		serializer = ToolCategorySerializer(data=cat_product)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

class RetrieveCategoryToolsAPIView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request):
		cats = ToolCategory.objects.filter(status=True)
		print(cats)
		serializer = ToolCategorySerializer(cats, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

class RetrieveUpdateDeleteCategoryToolsAPIView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request, cat_id):
		cat_obj = get_object_or_404(ToolCategory, pk=cat_id)
		serializer = ToolCategorySerializer(cat_obj)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def put(self, request, cat_id):
		cat_obj = get_object_or_404(ToolCategory, pk=cat_id)
		serializer_data = request.data.get('category_tool',{})
		serializer = ToolCategorySerializer(instance=cat_obj, data=serializer_data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_200_OK)

	def delete(self, request, cat_id):
		cat_obj = ToolCategory.objects.get(pk=cat_id)
		cat_obj.status = False
		cat_obj.save()
		serializer = ToolCategorySerializer(cat_obj)
		return Response(status=status.HTTP_200_OK)

	