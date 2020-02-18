from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.RetrieveProvidersListAPIView.as_view()),
    path('create/', views.CreateProviderAPIView.as_view()),
    path('<int:provider_id>/', views.RetrieveUpdateDeleteProviderAPIView.as_view()),
]