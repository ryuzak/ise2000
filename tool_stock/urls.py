from django.urls import path
from . import views

urlpatterns = [
	path('', views.RetrieveToolStockAPIView.as_view()),
	path('<slug:tool_model>/', views.RetrieveToolModelAPIView.as_view()),
	path('lend/<slug:tool_model>/', views.RetrieveToolModelStockAPIView.as_view()),
	path('lend/name/<str:tool_name>/', views.RetrieveToolNameStockAPIView.as_view()),
	path('create/initial/', views.CreateToolStockInitialAPIView.as_view()),
]