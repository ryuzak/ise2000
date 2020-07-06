from rest_framework import serializers

from tools.serializers import ToolSerializer
from ferreteria_back.base64 import  Base64FileField

from .models import ToolLend, ToolLendbridge
from accounts.serializers import UserSerializer
from building_work.serializers import BuildingWorkSerializer

class ToolLendSerializer(serializers.ModelSerializer):
	lend_date = serializers.DateField(required=True)

	class Meta:
		model = ToolLend
		fields = ('id', 'lend_date', 'building', 'user', 'return_date', 'notes', 'status', )

	def to_representation(self, instance):
		response = super().to_representation(instance)
		response['user'] = UserSerializer(instance.user).data
		response['building'] = BuildingWorkSerializer(instance.building).data
		return response

	def create(self, validated_data):
		toollend = ToolLend(
			lend_date = validated_data.get('lend_date', None),
			building = validated_data.get('building', ''),
			user = validated_data.get('user', ''),
			return_date = validated_data.get('return_date', None),
		)
		toollend.save()
		return toollend

	def update(self, instance, validated_data):
		instance.lend_date = validated_data.get('lend_date', instance.lend_date)
		instance.return_date = validated_data.get('return_date', instance.return_date)
		instance.notes = validated_data.get('notes', instance.notes)
		instance.status = validated_data.get('status', False)
		print(instance.status)
		instance.save()
		print(instance.status)
		return instance

class ToolLendBridgeSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = ToolLendbridge
		fields = ('tool', 'lend', 'quantity', 'status', )

	def to_representation(self, instance):
		response = super().to_representation(instance)
		response['tool'] = ToolSerializer(instance.tool).data
		response['lend'] = ToolLendSerializer(instance.lend).data
		return response

class ToolLendPDFSerializer(serializers.Serializer):
	file_name = serializers.CharField(max_length=250)
	file = Base64FileField(required=False)