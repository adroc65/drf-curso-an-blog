"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

# Importaciones para DRF_YASG:
# https://drf-yasg.readthedocs.io/en/stable/readme.html#installation
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# from posts.api.views import PostApiView  # Se va a usar ViewSets
from posts.api.router import router_post    # Se importa sistema de retas de ViewSets.


# SCHEMA para DRF_YASG:
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
    # Se comentan los permisos
    # permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router_post.urls)),        # Sistema de rutas de VIEWSETS
    # path('api/posts/', PostApiView.as_view()),    # Se usaba en APIViews
    path('api/', include('user.api.router')),       # Se da la ruta a los Token.

    # PATHS para DRF_YASG:
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
