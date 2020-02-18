from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.BudgetCreateAPIView.as_view()),
    path('<int:budget_id>/', views.BudgetDetailAPIView.as_view()),
    path('build/<int:building_id>/', views.BudgetBuildingDetailAPIView.as_view()),
]
