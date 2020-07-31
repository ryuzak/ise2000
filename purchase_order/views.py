from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from django.shortcuts import get_object_or_404

from .serializers import PurchaseOrderProductSerializer, PurchaseOrderSerializer
from accounts.serializers import UserSerializer

from .models import PurchaseOrder, PurchaseOrderProduct
from product_stock.models import ProductStock
from exit_order.models import ExitOrderProduct, ExitOrder

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
        order_obj['created_by'] = request.user.pk
        order_obj['delivery_date'] = f'{order_obj["delivery_date"]}T00:00:00'
        serializer = PurchaseOrderSerializer(data=order_obj)
        serializer.is_valid(raise_exception=True)
        serializer.save(products=order_obj['products'])
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CreatePurchaseExitOrderAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        order_obj = request.data
        order_obj['created_by'] = request.user.pk
        order_obj['delivery_date'] = f'{order_obj["delivery_date"]}T00:00:00'
        serializer = PurchaseOrderSerializer(data=order_obj)
        serializer.is_valid(raise_exception=True)
        serializer.save(products=order_obj['products'])
        exitorder_id = 0
        for prod in order_obj['products']:
            prod_obj = ExitOrderProduct.objects.get(pk=prod['id'])
            exitorder_id = prod_obj.order.id
            prod_obj.parcial_left = 0
            prod_obj.parcial = False
            prod_obj.status = True
            prod_obj.parcial_quantity = prod_obj.quantity
            prod_obj.save()
        print(ExitOrderProduct.objects.filter(order_id=exitorder_id).count())
        if (ExitOrderProduct.objects.filter(order_id=exitorder_id, parcial=True).count() == 0):
            exitorder = ExitOrder.objects.get(pk=exitorder_id)
            exitorder.status = True
            exitorder.save()
        

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

