from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from django.shortcuts import get_object_or_404

from .serializers import PurchaseOrderProductSerializer, PurchaseOrderSerializer
from accounts.serializers import UserSerializer
from .models import PurchaseOrder, PurchaseOrderProduct

class RetrievePurchaseOrdersAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        list_obj = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(list_obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreatePurchaseOrderAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        print(request.data)
        order_obj = request.data
        order_obj['created_by'] = request.user.pk
        #order_obj['purchase_date'] = f'{order_obj["purchase_date"]}T00:00:00'
        order_obj['delivery_date'] = f'{order_obj["delivery_date"]}T00:00:00'
        serializer = PurchaseOrderSerializer(data=order_obj)
        serializer.is_valid(raise_exception=True)
        serializer.save(products=order_obj['products'])
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class RetrievePurshaseOrderAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, order_id):
        order_obj = get_object_or_404(PurchaseOrder, pk=order_id)
        serializer = PurchaseOrderSerializer(order_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #def put(self, request, order_id):
