from django.contrib import admin
from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto
admin.site.register(Categoria)
admin.site.register(SubCategoria)
admin.site.register(UnidadMedida)
admin.site.register(Producto)

