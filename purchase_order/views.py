from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from django.shortcuts import get_object_or_404

from .serializers import PurchaseOrderProductSerializer, PurchaseOrderSerializer
from accounts.serializers import UserSerializer

from .models import PurchaseOrder, PurchaseOrderProduct
from product_stock.models import ProductStock

class RetrievePurchaseOrdersAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        list_obj = PurchaseOrder.objects.filter(building__id=None)
        serializer = PurchaseOrderSerializer(list_obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RetrievePurchaseOrdersBuildingAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, building_id):
        list_obj = PurchaseOrder.objects.filter(building__id=building_id)
        serializer = PurchaseOrderSerializer(list_obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreatePurchaseOrderAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        order_obj = request.data
        print(order_obj)
        order_obj['created_by'] = request.user.pk
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

    def put(self, request, order_id):
        order_obj = get_object_or_404(PurchaseOrder, pk=order_id)
        data = request.data
        serializer = PurchaseOrderSerializer(instance=order_obj, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class RecievePurchaseOrderInventoryAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def put(self, request, order_id):
        order_obj = get_object_or_404(PurchaseOrder, pk=order_id)
        prodorder_list = PurchaseOrderProduct.objects.filter(order__pk=order_id)
        saved_product_list = []
        for prod in prodorder_list:
            if order_obj.building:
                stock_obj = get_object_or_404(ProductStock, product__id=prod.product.id)
                stock_obj.stock = stock_obj.stock + prod.quantity
                stock_obj.save()

            prod.status = True
            saved_product_list.append(prod)
            

        [x.save() for x in saved_product_list]
        order_obj.status = True
        order_obj.save()

        
        return Response({'status':'OK', 'message':'Orden ingresada con exito'}, status=status.HTTP_200_OK)

