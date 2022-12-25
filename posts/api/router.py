"""
En este archivo de rutas se deben de traer el archivo de VIEWS, para
referenciar las vistas y el Default Router de DRF.
"""

from rest_framework.routers import DefaultRouter

# from posts.api.views import PostViewSet
# Para usar ModelViewSet, se importa el modelo correspondiente:
from posts.api.views import PostModelViewSet

router_post = DefaultRouter()
router_post.register(prefix='posts', basename='posts', viewset=PostModelViewSet)
