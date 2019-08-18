from django.urls import path, re_path
from . import views

urlpatterns = [
	path('list/', views.RetreiveUsersAPIView.as_view()),
	path('create/', views.CreateUserAPIView.as_view()),
	path('<int:user_id>/', views.RetreiveUpdateUserAPIView.as_view()),
	#-- Activation Link User
    re_path(r'^activation/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.ActivationEmailUserAPIView.as_view(), name='accounts_activation'),
]