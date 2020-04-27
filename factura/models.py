from django.db import models
from bases.models import ClaseModelo

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