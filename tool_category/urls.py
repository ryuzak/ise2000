from django.urls import path
from . import views

urlpatterns = [
	path('create/', views.CreateCategoryToolsAPIView.as_view()),
	path('list/', views.RetrieveCategoryToolsAPIView.as_view()),
	path('<int:cat_id>/', views.RetrieveUpdateDeleteCategoryToolsAPIView.as_view()),
]