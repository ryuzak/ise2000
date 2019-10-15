from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from .serializers import PurchaseOrderProductSerializer, PurchaseOrderSerializer
from accounts.serializers import UserSerializer
from .models import PurchaseOrder, PurchaseOrderProduct

class RetrievePurchaseOrdersAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        list_obj = PurchaseOrder.objects.all()
        print(list_obj)
        serializer = PurchaseOrderSerializer(list_obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreatePurchaseOrderAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        order_obj = request.data
        order_obj['created_by'] = request.user.pk
        order_obj['delivery_date'] = f'{order_obj["delivery_date"]}T00:00:00'
        serializer = PurchaseOrderSerializer(data=order_obj)
        serializer.is_valid(raise_exception=True)
        serializer.save(products=order_obj['products'])
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)