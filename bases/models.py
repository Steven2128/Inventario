from django.db import models
from django.contrib.auth.models import User
from django_userforeignkey.models.fields import UserForeignKey

class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE)
    usuario_modificacion = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True


class ClaseModelo2(models.Model):
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_creacion = UserForeignKey(auto_user_add=True, related_name='+')
    usuario_modificacion = UserForeignKey(auto_user=True, related_name='+')

    class Meta:
        abstract = True