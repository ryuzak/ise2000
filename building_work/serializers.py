from rest_framework import serializers

from .models import BuildingWork

class BuildingWorkSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = BuildingWork
		fields = ('id', 'client_name', 'contact_name', 'project_name', 'location', 'contact_mail', 'contact_phone', 'status')

	def create(self, validated_data):
		buildingwork = BuildingWork(
			client_name = validated_data['client_name'],
			contact_name = validated_data['contact_name'],
			project_name = validated_data['project_name'],
			location = validated_data['location'],
			contact_mail = validated_data['contact_mail'],
			contact_phone = validated_data['contact_phone']
		)

		buildingwork.save()
		return buildingwork