from django import forms
from bootstrap_modal_forms.forms import BSModalForm
from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        labels = {
            'descripcion': ''
        }
        widgets = {
            'descripcion': forms.TextInput(
                attrs={'placeholder': 'Descripción de la categoría', 'size': '45'})
        }

        
class SubCategoriaForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
            queryset=Categoria.objects.filter(estado=True).order_by('descripcion'))
    class Meta:
        model = SubCategoria
        fields = ['descripcion', 'categoria']
        labels = { 'descripcion': 'Subcategoría', 'categoria': ''}
        widgets = {
            'descripcion': forms.TextInput(
                attrs={'placeholder': 'Descripción de la subcategoría', 'size': '30'})
        }

    def __init__(self, *args, **kwargs):
        super(SubCategoriaForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].empty_label = 'Seleccione categoría'

    
class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['descripcion']
        labels = {'descripcion': ''}
        widgets = {'descripcion': forms.TextInput(
            attrs = {'placeholder': 'Descripcion de la marca'})
        }


class UnidadMedidaForm(forms.ModelForm):
    class Meta:
        model = UnidadMedida
        fields = ['descripcion']
        labels = {'descripcion': ''}
        widgets = {'descripcion': forms.TextInput(
            attrs= {'placeholder': 'Descripcion de la unidad de medida'})
        }


class ProdutoForm(BSModalForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'codigo_barra', 'descripcion',
        'precio', 'existencia', 'ultima_compra', 'marca', 
        'subcategoria', 'unidad_medida']

        exclude = ['usuario_modificacion', 'fecha_modificacion', 
        'usuario_creacion', 'fecha_creacion']
        widget = {
            'descipcion': forms.TextInput()
        }

    def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)
        self.fields['ultima_compra'].widget.attrs['readonly'] = True
        self.fields['existencia'].widget.attrs['readonly'] = True