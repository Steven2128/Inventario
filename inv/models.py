from django.db import models
from bases.models import ClaseModelo

class Categoria(ClaseModelo):
    descripcion = models.CharField(max_length=100, help_text='Descripción de la categoría', unique=True)


    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = 'Categorias'