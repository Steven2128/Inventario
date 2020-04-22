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


class Producto(ClaseModelo):
    codigo = models.CharField(max_length=20, unique=True)
    codigo_barra = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.FloatField(default=0)
    existencia = models.IntegerField(default=0)
    ultima_compra = models.DateField(null=True, blank=True)

    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Producto, self).save()

    class Meta:
        verbose_name_plural = 'Productos'
        unique_together = ('codigo', 'codigo_barra')