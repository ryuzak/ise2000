from django.utils.crypto import get_random_string
from ferreteria_back.base64 import  Base64ImageField
from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
	date_joined = serializers.ReadOnlyField()
	picture = Base64ImageField(required=False)

	class Meta(object):
		model = User
		fields = ('id','email', 'first_name', 'last_name', 'phone', 'date_joined', 'is_active', 'position', 'picture')
		#extra_kwargs = {'password':{'write_only':True}}

	def create(self, validated_data):
		user = User(
			email = validated_data['email'],
			first_name = validated_data['first_name'],
			last_name = validated_data['last_name'],
			phone = validated_data['phone'],
			position = validated_data['position'],
			picture = validated_data['picture'],
			is_active = True
		)
		password = get_random_string(15)
		user.set_password(password)
		user.save()
		user.activation_email('dev.r0bmtz.com',user,password)
		return user

	# def update(self, instance, validated_data):
	# 	print(validated_data)
	# 	print(instance)
	# 	instance.email = validated_data.get('email', instance.email)
	# 	instance.first_name = validated_data.get('first_name', instance.first_name),
	# 	instance.last_name = validated_data.get('last_name', instance.last_name),
	# 	instance.phone = validated_data.get('phone', instance.phone)

	# 	instance.save()
	# 	return instance