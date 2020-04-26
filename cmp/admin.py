from django.contrib import admin
from .models import Proveedor, ComprasDet, ComprasEnc

admin.site.register(Proveedor)
admin.site.register(ComprasEnc)
admin.site.register(ComprasDet)