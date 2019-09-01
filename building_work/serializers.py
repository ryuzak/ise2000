from rest_framework import serializers

from .models import BuildingWork
from accounts.serializers import UserSerializer

class BuildingWorkSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = BuildingWork
		fields = ('id', 'client_name', 'contact_name', 'project_name', 'location', 'contact_mail', 'contact_phone', 'status', 'user')

	def to_representation(self, instance):
		response = super().to_representation(instance)
		response['user'] = UserSerializer(instance.user).data
		return response

	def create(self, validated_data):
		buildingwork = BuildingWork(
			client_name = validated_data.get('client_name', ''),
			contact_name = validated_data.get('contact_name', ''),
			project_name = validated_data.get('project_name', ''),
			location = validated_data.get('location', ''),
			contact_mail = validated_data.get('contact_mail',''),
			contact_phone = validated_data.get('contact_phone',''),
			user = validated_data.get('user', '')
		)

		buildingwork.save()
		return buildingwork

	def update(self, instance, validated_data):
		instance.client_name = validated_data.get('client_name', '')
		instance.contact_name = validated_data.get('contact_name', '')
		instance.project_name = validated_data.get('project_name', '')
		instance.location = validated_data.get('location', '')
		instance.contact_mail = validated_data.get('contact_mail', '')
		instance.contact_phone = validated_data.get('contact_phone', '')
		instance.user = validated_data.get('user', '')
		
		instance.save()

		return instance

