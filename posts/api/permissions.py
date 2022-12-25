"""
En este archivo se crean los permisos personalizados, esto
se hace por si se ve la necesidad de crear un tipo de permiso
que no existe en el ModelView.

Luego el permiso se debe de importat en las VIEWS.

"""

from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        else:
            return request.user.is_staff
