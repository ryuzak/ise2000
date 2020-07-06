from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.ConceptListAPIView.as_view()),
    path('create/', views.ConceptCreateAPIView.as_view()),
    path('<int:concept_id>/', views.ConceptRetrieveUpdateDeleteAPIView.as_view()),
    path('products/<int:concept_id>/', views.ConceptProductsRetrieveAPIView.as_view()),
]