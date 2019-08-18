from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from .serializers import UserSerializer
from .models import User

class CreateUserAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
    	serializer = UserSerializer(request.user)
    	print(serializer.data)
    	return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user = request.data
        print(user)
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class RetreiveUsersAPIView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request):
		users = User.objects.filter(is_active=True)
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

class RetreiveUpdateUserAPIView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request, user_id):
		serializer = UserSerializer(User.objects.get(pk=user_id))
		return Response(serializer.data, status=status.HTTP_200_OK)

	def put(self, request, user_id):
		user_obj = User.objects.get(pk=user_id)
		serializer_data = request.data
		serializer = UserSerializer(instance=user_obj, data=serializer_data, partial=True)
		print(serializer_data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		print('saved')
		return Response(serializer.data, status=status.HTTP_200_OK)

	def delete(self, request, user_id):
		user_obj = User.objects.get(pk=user_id)
		user_obj.is_active = False
		user_obj.save()
		serializer = UserSerializer(user_obj)
		return Response(serializer.data, status=status.HTTP_200_OK)

class ActivationEmailUserAPIView(APIView):
	permission_classes = (AllowAny,)

	def get(self, request, uidb64, token):

		user_activation = User.actiavation_url(uidb64, token)

		return Response({'actiation':user_activation}, status=status.HTTP_200_OK)