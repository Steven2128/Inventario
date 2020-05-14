from django.contrib import admin
from .models import Cliente, FacturaDet, FacturaEnc
admin.site.register(Cliente)
admin.site.register(FacturaDet)
admin.site.register(FacturaEnc)