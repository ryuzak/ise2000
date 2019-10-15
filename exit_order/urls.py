from django.urls import path

from . import views 

urlpatterns = [
	path('list/', views.RetrieveExitOrderListAPIView.as_view()),
	path('create/', views.CreateOrderAPIView.as_view()),
]