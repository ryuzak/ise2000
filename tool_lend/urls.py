from django.urls import path

from . import views

urlpatterns = [
	path('', views.CreateRetrieveToolLendsAPIView.as_view()),
	path('<int:lend_id>/', views.RetrieveUpdateToolLendsAPIView.as_view()),
	path('settools/<int:lend_id>/', views.RetrieveToolLendsAPIView.as_view()),
]