from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from django.shortcuts import get_object_or_404

from provider.serializers import ProviderSerializer
from provider.models import Provider

class RetrieveProvidersListAPIView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request):
		providers = Provider.objects.filter(status=True)
		serializer = ProviderSerializer(providers, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class CreateProviderAPIView(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self, request):
		data = request.data
		serializer = ProviderSerializer(data=data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

class RetrieveUpdateDeleteProviderAPIView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request, provider_id):
		provider = get_object_or_404(Provider, pk=provider_id)
		serializer = ProviderSerializer(provider)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def put(self, request, provider_id):
		provider = get_object_or_404(Provider, pk=provider_id)
		data = request.data
		serializer = ProviderSerializer(instance=provider, data=data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_200_OK)

	def delete(self, request, provider_id):
		provider = get_object_or_404(Provider, pk=provider_id)
		provider.status = False
		provider.save()
		serializer = ProviderSerializer(provider)
		return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)