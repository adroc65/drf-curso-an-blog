from django.db import models


# Create your models here.
class Post(models.Model):
    """Post object."""
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default='1', verbose_name='Orden en que se muestra')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    def __str__(self):
        return self.title
