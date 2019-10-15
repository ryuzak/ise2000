from django.urls import path
from . import views

urlpatterns = [
	path('', views.RetrieveProductStockAPIView.as_view()),
	path('<slug:prod_code>/', views.RetrieveRegisterProductCodeAPIView.as_view()),
	path('get/<slug:prod_code>/', views.RetrieveProductCodeAPIView.as_view()),
	path('create/initial/', views.CreateProductStockInitialAPIView.as_view()),
]