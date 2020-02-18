from django.urls import path

from . import views 

urlpatterns = [
	path('list/', views.RetrieveExitOrderListAPIView.as_view()),
	path('create/', views.CreateOrderAPIView.as_view()),
	path('<int:order_id>/', views.RetrieveOrderAPIView.as_view()),
	path('products/<int:order_id>/', views.RetrieveOrderPRoductsAPIView.as_view()),
]