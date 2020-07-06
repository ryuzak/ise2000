from django.urls import path
from . import views

urlpatterns = [
	path('list/', views.RetrieveProductsAPIView.as_view()),
	path('list/<str:name_query>/', views.RetrieveProductsNameAPIView.as_view()),
	path('list/description/<str:description_query>/', views.RetrieveProductsDescriptionAPIView.as_view()),
	path('create/', views.CreateProductAPIView.as_view()),
	path('<int:prod_id>/', views.RetrieveUpdateDeleteProductAPIView.as_view()),
]