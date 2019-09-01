from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from django.shortcuts import get_object_or_404

from .serializers import BuildingWorkSerializer
from .models import BuildingWork

class CreateBuildingWorkAPIView(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self, request):
		building_obj = request.data
		serializer = BuildingWorkSerializer(data=building_obj)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

class RetrieveBuildingWorksAPIView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self,request):
		stock = BuildingWork.objects.filter(status=True)
		serializer = BuildingWorkSerializer(stock, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

class RetrieveUpdateDeleteBuildingWorkAPIView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request, building_id):
		building_obj = get_object_or_404(BuildingWork, pk=building_id)
		serializer = BuildingWorkSerializer(building_obj)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def put(self, request, building_id):
		building_obj = get_object_or_404(BuildingWork, pk=building_id)
		serializer_data = request.data.get('building',{})
		user_id = serializer_data['user']['id']
		del serializer_data['user']
		serializer_data['user'] = user_id
		serializer = BuildingWorkSerializer(instance=building_obj, data=serializer_data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_200_OK)

	def delete(self, request, building_id):
		building_obj = BuildingWork.objects.get(pk=building_id)
		building_obj.status = False
		building_obj.save()
		serializer = BuildingWorkSerializer(building_obj)
		return Response(serializer.data, status=status.HTTP_200_OK)