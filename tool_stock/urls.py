from django.urls import path
from . import views

urlpatterns = [
	path('', views.RetrieveToolStockAPIView.as_view()),
	path('<slug:tool_model>/', views.RetrieveToolModelAPIView.as_view()),
	path('create/initial/', views.CreateToolStockInitialAPIView.as_view()),
]