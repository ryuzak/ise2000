from django.urls import path
from . import views

urlpatterns = [
	path('list/', views.RetrieveToolsAPIView.as_view()),
	path('create/', views.CreateToolAPIView.as_view()),
	path('<int:tool_id>/', views.RetrieveUpdateDeleteToolAPIView.as_view()),
]