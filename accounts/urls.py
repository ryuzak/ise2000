from django.urls import path
from . import views

urlpatterns = [
	path('list/', views.RetreiveUsersAPIView.as_view()),
	path('create/', views.CreateUserAPIView.as_view()),
	path('<int:user_id>/', views.RetreiveUpdateUserAPIView.as_view()),
]