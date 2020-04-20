from django.db import models
from bases.models import ClaseModelo

class Categoria(ClaseModelo):
    descripcion = models.CharField(max_length=100, help_text='Descripción de la categoría', unique=True)


    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = 'Categorias'


class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)


    def __str__(self):
        return self.categoria.descripcion+':'+self.descripcion
    
    class Meta:
        verbose_name_plural = 'Sub Categorias'
        unique_together = ('categoria', 'descripcion')


class Marca(ClaseModelo):
    descripcion = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = 'Marcas'


class UnidadMedida(ClaseModelo):
    descripcion = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = 'Unidades de medidas'