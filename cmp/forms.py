from django import forms
from .models import Proveedor, ComprasEnc
from bootstrap_modal_forms.forms import BSModalForm

class ProveedorForm(BSModalForm):
    email = forms.EmailField(max_length=254)
    class Meta:
        model = Proveedor
        exclude = ['usuario_creacion', 'fecha_creacion', 'usuario_modificacion', 'fecha_modificacion', 'estado']
        widget = {'descripcion': forms.TextInput()}



class ComprasEncForm(forms.ModelForm):
    fecha_compra = forms.DateInput()
    fecha_factura = forms.DateInput()

    class Meta:
        model = ComprasEnc
        fields = ['proveedor', 'fecha_compra', 'observacion',
        'no_factura', 'fecha_factura', 'sub_total', 'descuento',
        'total']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['fecha_compra'].widget.attrs.update({'autocomplete': 'off'})
        self.fields['fecha_factura'].widget.attrs.update({'autocomplete': 'off'})
        self.fields['sub_total'].widget.attrs['readonly'] = True
        self.fields['descuento'].widget.attrs['readonly'] = True
        self.fields['total'].widget.attrs['readonly'] = True
