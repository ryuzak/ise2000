from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from .serializers import ExitOrderProductSerializer, ExitOrderSerializer
from .models import ExitOrder

from accounts.serializers import UserSerializer

class RetrieveExitOrderListAPIView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request):
		order_list = ExitOrder.objects.all()
		serializer = ExitOrderSerializer(order_list, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class CreateOrderAPIView(APIView):
	permission_classes = (IsAuthenticated, )

	def post(self, request):
		order_obj = request.data
		serializer = ExitOrderSerializer(data=order_obj)
		serializer.is_valid(raise_exception=True)
		serializer.save(request=request, products=order_obj['products'])
		return Response(serializer.data, status=status.HTTP_201_CREATED)