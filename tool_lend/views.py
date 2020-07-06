from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from .models import ToolLend, ToolLendbridge
from .serializers import ToolLendSerializer, ToolLendBridgeSerializer

class CreateRetrieveToolLendsAPIView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request):
		lend_list = ToolLend.objects.all()
		serializer = ToolLendSerializer(lend_list, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request):
		lend_obj = request.data
		serializer = ToolLendSerializer(data=lend_obj)
		serializer.is_valid(raise_exception=True)
		serializer.save()

		toollend = serializer.instance
		tools = lend_obj['tools']

		bulk = list(map(lambda x: ToolLendbridge(lend=toollend, quantity=x['quantity'], tool_id=x['id']), tools))
		ToolLendbridge.objects.bulk_create(bulk)
		
		return Response(serializer.data, status=status.HTTP_201_CREATED)

class RetrieveToolLendsUserAPIView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request, user_id):
		print(ToolLend.objects.filter(user_id=user_id))
		lend_list = ToolLend.objects.filter(user__pk = user_id)
		serializer = ToolLendSerializer(lend_list, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

class RetrieveUpdateToolLendsAPIView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request, lend_id):
		lend_obj = ToolLend.objects.get(pk=lend_id)
		serializer = ToolLendSerializer(lend_obj)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def put(self, request, lend_id):
		try:
			lend_obj = ToolLend.objects.get(pk=lend_id)
		except ToolLend.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		serializer_data = request.data
		serializer_data['user'] = serializer_data['user']['id']
		serializer_data['building'] = serializer_data['building']['id']
		serializer = ToolLendSerializer(instance=lend_obj, data=serializer_data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		print(serializer.data)
		return Response(serializer.data, status=status.HTTP_200_OK)

class RetrieveToolLendsAPIView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request, lend_id):
		tools_list = ToolLendbridge.objects.filter(lend__id=lend_id)
		serializer = ToolLendBridgeSerializer(tools_list, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

