from django.urls import path
from . import views

urlpatterns = [
	path('create/', views.CreateBuildingWorkAPIView.as_view()),
	path('list/', views.RetrieveBuildingWorksAPIView.as_view()),
	path('<int:building_id>/', views.RetrieveUpdateDeleteBuildingWorkAPIView.as_view()),
]