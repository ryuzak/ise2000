from django.urls import path

from . import views

urlpatterns = [
	path('list/', views.RetrievePurchaseOrdersAPIView.as_view()),
	path('create/', views.CreatePurchaseOrderAPIView.as_view()),
]