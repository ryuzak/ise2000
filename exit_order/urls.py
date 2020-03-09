from django.urls import path

from . import views 

urlpatterns = [
	path('list/', views.RetrieveExitOrderListAPIView.as_view()),
	path('create/', views.CreateOrderAPIView.as_view()),
	path('<int:order_id>/', views.RetrieveOrderAPIView.as_view()),
	path('products/<int:order_id>/', views.RetrieveOrderPRoductsAPIView.as_view()),
	path('products/prodive/<int:order_id>/', views.GiveTotalExitOrderAPIView.as_view()),
	path('building/<int:building_id>/', views.RetrieveExitOrderBuildingListAPIView.as_view()),
]