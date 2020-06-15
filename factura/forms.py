from django import forms
from .models import Cliente
from bootstrap_modal_forms.forms import BSModalForm

class ClienteForm(BSModalForm):
    class Meta:
        model = Cliente
        fields = ['nombres', 'apellidos', 'telefono', 'tipo']
        exclude = ['usuario_modificacion', 'fecha_modificacion', 
        'usuario_creacion', 'fecha_creacion']