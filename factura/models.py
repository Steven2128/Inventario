from django.db import models
from bases.models import ClaseModelo, ClaseModelo2
from inv.models import Producto

class Cliente(ClaseModelo):
    NAT='Natural'
    JUR='Jurídica'
    TIPO_CLIENTE = [
        (NAT, 'Natural'),
        (JUR, 'Jurídica')
    ]
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    tipo = models.CharField(max_length=10, choices=TIPO_CLIENTE, default=NAT)

    def __str__(self):
        return '{} {}'.format(self.nombres, self.apellidos)

    def save(self):
        self.nombres = self.nombres.upper()
        self.apellidos = self.apellidos.upper()
        super(Cliente, self).save()

    class Meta:
        verbose_name_plural = 'Clientes'


class FacturaEnc(ClaseModelo2):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    sub_total = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)

    def __str__(self):
        return self.id

    def save(self):
        self.total = self.sub_total - self.descuento
        super(FacturaEnc, self).save()

    class meta:
        verbose_name_plural = 'Encabezado Facturas'
        verbose_name = 'Encabezado Factura'


class FacturaDet(ClaseModelo2):
    factura = models.ForeignKey(FacturaEnc, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.BigIntegerField(default=0)
    precio = models.FloatField(default=0)
    sub_total = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)

    def __str__(self):
        return self.producto

    def save(self):
        self.sub_total = float(float(int(self.cantidad)) * float(self.precio))
        self.total = self.sub_total - self.descuento
        super(FacturaEnc, self).save()

    class meta:
        verbose_name_plural = 'Detalles facturas'
        verbose_name = 'Detalle Factura'