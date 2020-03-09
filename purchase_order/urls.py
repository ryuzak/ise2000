from django.urls import path

from . import views

urlpatterns = [
	path('list/', views.RetrievePurchaseOrdersAPIView.as_view()),
	path('create/', views.CreatePurchaseOrderAPIView.as_view()),
	path('<int:order_id>/', views.RetrievePurchaseOrdersAPIView.as_view()),
	path('ingress/<int:order_id>/', views.RecievePurchaseOrderInventoryAPIView.as_view()),
	path('building/<int:building_id>/', views.RetrievePurchaseOrdersBuildingAPIView.as_view()),
]