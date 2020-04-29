from django import forms
from .models import Cliente
from inv.models import Producto
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombres', 'apellidos', 'telefono', 'tipo']
        exclude = ['usuario_modificacion', 'fecha_modificacion', 
        'usuario_creacion', 'fecha_creacion']
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })