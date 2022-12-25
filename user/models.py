"""
Haciendo Overdrive de los usuarios de Django.
1. Se crea la APP 'users', y se crea el modelo.
2. En el Setting.py se debe de indicar que esta app se usa para manejar usuarios.
3. Ahora lo mejor es borrar el archivo de SQLITE3 y todas las migraciones.
4. Volver a hacer las migraciones.
5. Ahora se debe de volver a agregar USER en el panel de administración, 'admin.py'.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
)


class User(AbstractUser):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
