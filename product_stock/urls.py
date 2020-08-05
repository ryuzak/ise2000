from django.urls import path
from . import views

urlpatterns = [
	path('', views.RetrieveProductStockAPIView.as_view()),
	path('<int:prod_id>/', views.ReterieveProductIdAPIView.as_view()),
	path('code/<slug:prod_code>/', views.RetrieveRegisterProductCodeAPIView.as_view()),
	path('get/<slug:prod_code>/', views.RetrieveProductCodeAPIView.as_view()),
	path('create/initial/', views.CreateProductStockInitialAPIView.as_view()),
	path('name/<str:prod_name>/', views.RetrieveProductNameListAPIView.as_view()),
	path('description/<str:description_query>/', views.RetrieveProductDecriptionListAPIView.as_view()),
]