from django.urls import path
from . import views

urlpatterns = [
	path('list/', views.RetrieveProductsAPIView.as_view()),
	path('create/', views.CreateProductAPIView.as_view()),
	path('<int:prod_id>/', views.RetrieveUpdateDeleteProductAPIView.as_view()),
]