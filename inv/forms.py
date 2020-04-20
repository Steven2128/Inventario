from django import forms
from .models import Categoria, SubCategoria, Marca, UnidadMedida

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado']
        labels = {'descripcion': 'Descripción de la categoría', 'estado': 'Estado'}
        widget = {'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

        
class SubCategoriaForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(estado=True).order_by('descripcion')
        )
    class Meta:
        model = SubCategoria
        fields = ['categoria', 'descripcion', 'estado']
        labels = {'descripcion': 'Subcategoría', 'estado': 'Estado'}
        widget = {'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['categoria'].empty_label = 'Seleccione categoría'

    
class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['descripcion', 'estado']
        labels = {'descripcion': 'Descripcion de la marca', 'estado': 'Estado'}
        widgets = {'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class UnidadMedidaForm(forms.ModelForm):
    class Meta:
        model = UnidadMedida
        fields = ['descripcion', 'estado']
        labels = {
            'descripcion': 'Descripcion de la unidad de medida', 'estado': 'Estado'
        }
        widgets = {'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })