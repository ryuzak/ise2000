"""ferreteria_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
  #  path('admin/', admin.site.urls),
    path('auth-jwt/', obtain_jwt_token),
    path('auth-jwt-refresh/', refresh_jwt_token),
    path('auth-jwt-verify/', verify_jwt_token),
    path('users/', include('accounts.urls',)),
    path('category/products/', include('product_category.urls',)),
    path('category/tools/', include('tool_category.urls',)),
    path('stock/products/', include('product_stock.urls',)),
    path('stock/tools/', include('tool_stock.urls',)),
    path('products/', include('products.urls',)),
    path('tools/', include('tools.urls',)),
    path('buildingwork/', include('building_work.urls',)),
    path('lend/tools/', include('tool_lend.urls',)),
    path('order/exit/', include('exit_order.urls',)),
    path('order/purchase/', include('purchase_order.urls',)),
    path('providers/', include('provider.urls',)),
    path('budgets/', include('budget.urls',)),
    path('concepts/', include('prebuild_concepts.urls',)),

    re_path(r'^swagger(?P<format>\.json|\.yaml|\.xml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]						
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)