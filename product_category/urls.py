from django.urls import path
from . import views

urlpatterns = [
	path('create/', views.CreateCategoryProductAPIView.as_view()),
	path('list/', views.RetrieveCategoryProductsAPIView.as_view()),
	path('<int:cat_id>/', views.RetrieveUpdateDeleteCategoryProductsAPIView.as_view()),
]