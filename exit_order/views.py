from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from .models import ExitOrder, ExitOrderProduct
from product_stock.models import ProductStock

from .serializers import ExitOrderProductSerializer, ExitOrderSerializer
from accounts.serializers import UserSerializer

class RetrieveExitOrderListAPIView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request):
		order_list = ExitOrder.objects.filter(building=None)
		serializer = ExitOrderSerializer(order_list, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class RetrieveExitOrderBuildingListAPIView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request, building_id):
		order_list = ExitOrder.objects.filter(building__id=building_id)
		serializer = ExitOrderSerializer(order_list, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class CreateOrderAPIView(APIView):
	permission_classes = (IsAuthenticated, )

	def post(self, request):
		order_obj = request.data
		print(request.data)
		serializer = ExitOrderSerializer(data=order_obj)
		serializer.is_valid(raise_exception=True)
		serializer.save(request=request, products=order_obj['products'])
		return Response(serializer.data, status=status.HTTP_201_CREATED)


class RetrieveOrderAPIView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request, order_id):
		order_obj = ExitOrder.objects.get(pk=order_id)
		order_obj.exitorderproduct_set.all()
		serializer = ExitOrderSerializer(order_obj)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def put(self, request, order_id):
		data = request.data
		order_obj = get_object_or_404(ExitOrder, pk=order_id)
		stock_list = []
		prod_list = []
		order_obj.parcial = False
		order_obj.status = True
		for prod in data['products']:
			prod_obj = ExitOrderProduct.objects.get(pk=prod['id'])
			prod_stock = ProductStock.objects.get(product__id=prod['product']['id'])
			
			if prod_stock.stock < int(prod['parcial_quantity']):
				return Response({'status':'WARN','messgae':'Inventario insuficiente'}, status=status.HTTP_400_BAD_REQUEST)
			else:
				if(int(prod['parcial_quantity']) < prod_obj.parcial_left):
					print('left')
					prod_obj.parcial_quantity = prod_obj.parcial_quantity + int(prod['parcial_quantity'])
					prod_obj.parcial_left = prod_obj.parcial_left - int(prod['parcial_quantity'])
					prod_obj.parcial = True
					order_obj.status = False
					order_obj.parcial = True
				elif (prod_obj.parcial_left ==  int(prod['parcial_quantity'])):
					print('complete')
					prod_obj.parcial_left = 0
					prod_obj.parcial = False
					prod_obj.status = True
					prod_obj.parcial_quantity = prod_obj.quantity

				prod_list.append(prod_obj)
				
				prod_stock.stock = prod_stock.stock - int(prod['parcial_quantity'])
				stock_list.append(prod_stock)
		
		[x.save() for x in prod_list]
		[x.save() for x in stock_list]
		order_obj.save()
		serializer = ExitOrderSerializer(order_obj)
		return Response(serializer.data, status=status.HTTP_200_OK)


class RetrieveOrderPRoductsAPIView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request, order_id):
		prods = ExitOrderProduct.objects.filter(order__pk=order_id)
		serializer = ExitOrderProductSerializer(prods, many=True)
		print(serializer.data)
		return Response(serializer.data, status=status.HTTP_200_OK)


class GiveTotalExitOrderAPIView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request, order_id):
		order_obj = ExitOrder.objects.get(pk=order_id, status=False)
		product_list = ExitOrderProduct.objects.filter(order_id=order_id, status=False)
		stock_list = []
		prod_list = []
		for prod in product_list:
			stock_obj = ProductStock.objects.get(product_id=prod.product.id)
			if stock_obj.stock < prod.quantity:
				return Response({'status':'WARN', 'message':'No cuenta con inventario suficiente'}, status=status.HTTP_400_BAD_REQUEST)
			else:
				if prod.parcial:
					stock_obj.stock = stock_obj.stock - (prod.quantity - prod.parcial_quantity)
					prod.parcial = False
				else:
					stock_obj.stock = stock_obj.stock - prod.quantity
				stock_list.append(stock_obj)
				prod.status = True
				prod.parcial = False
				prod.parcial_left = 0
				prod_list.append(prod)

		[x.save() for x in stock_list]
		[x.save() for x in prod_list]
		order_obj.status = True
		order_obj.save()
		return Response({'status':'OK', 'message':'Orden surtida con exito'}, status=status.HTTP_200_OK)

