from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto
from .forms import CategoriaForm, SubCategoriaForm, MarcaForm, UnidadMedidaForm, ProdutoForm


class CategoriaView(LoginRequiredMixin, generic.ListView):
    model = Categoria
    template_name = 'inv/categoria_list.html'
    context_object_name = 'obj'
    login_url = 'login'


class CategoriaNew(LoginRequiredMixin, generic.CreateView):
    template_name = 'inv/categoria_form.html'
    form_class = CategoriaForm
    login_url = 'login'

    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)


class CategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Categoria
    template_name = 'inv/categoria_form.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('categoria_list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        return super().form_valid(form)


class CategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model = Categoria
    template_name = 'inv/categoria_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('categoria_list')
    login_url = 'login'


class SubCategoriaView(LoginRequiredMixin, generic.ListView):
    model = SubCategoria
    template_name = 'inv/subcategoria_list.html'
    context_object_name = 'obj'
    login_url = 'login'


class SubCategoriaNew(LoginRequiredMixin, generic.CreateView):
    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    success_url = reverse_lazy('subcategoria_list')
    form_class = SubCategoriaForm
    login_url = 'login'

    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)


class SubCategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    form_class = SubCategoriaForm
    success_url = reverse_lazy('subcategoria_list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        return super().form_valid(form)


class SubCategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model = SubCategoria
    template_name = 'inv/categoria_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('subcategoria_list')
    login_url = 'login'


class MarcaView(LoginRequiredMixin, generic.ListView):
    model = Marca
    template_name = 'inv/marca_list.html'
    context_object_name = 'obj'
    login_url = 'login'


class MarcaNew(LoginRequiredMixin, generic.CreateView):
    model = Marca
    template_name = 'inv/marca_form.html'
    form_class = MarcaForm
    success_url = reverse_lazy('marca_list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)


class MarcaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Marca
    template_name = 'inv/marca_form.html'
    form_class = MarcaForm
    success_url = reverse_lazy('marca_list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        return super().form_valid(form)

@login_required 
def marca_inactivar(request, id):
    model = Marca.objects.filter(pk=id).first() 
    if request.method == 'GET': 
        if model.estado ==True: 
            model.estado = False
            messages.success(request, 'Marca inactivada')
        else: 
            model.estado = True
            messages.success(request, 'Marca activada')
        model.save()
        
    return redirect('marca_list')


class UnidadMedidaView(LoginRequiredMixin, generic.ListView):
    model = UnidadMedida
    template_name = 'inv/um_list.html'
    context_object_name = 'obj'
    login_url = 'login'


class UnidadMedidaNew(LoginRequiredMixin, generic.CreateView):
    template_name = 'inv/um_form.html'
    form_class = UnidadMedidaForm
    success_url = reverse_lazy('um_list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)


class UnidadMedidaEdit(LoginRequiredMixin, generic.UpdateView):
    model = UnidadMedida
    template_name = 'inv/um_form.html'
    form_class = UnidadMedidaForm
    success_url = reverse_lazy('um_list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        return super().form_valid(form)

@login_required
def u_m_inactivar(request, id):
    model = UnidadMedida.objects.filter(pk=id).first()
        
    if request.method == 'GET':
        if model.estado ==True:
            model.estado = False
            messages.success(request, 'Unidad de medida inactivada')
        else:
            model.estado = True
            messages.success(request, 'Unidad de medida inactivada')
        model.save()
    return redirect('um_list')


class ProductoView(LoginRequiredMixin, generic.ListView):
    model = Producto
    template_name = 'inv/product_list.html'
    context_object_name = 'obj'
    login_url = 'login'


class ProductoNew(LoginRequiredMixin, generic.CreateView):
    model = Producto
    template_name = 'inv/producto_form.html'
    form_class = ProdutoForm
    success_url = reverse_lazy('producto_list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)


class ProductoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Producto
    template_name = 'inv/producto_form.html'
    form_class = ProdutoForm
    success_url = reverse_lazy('producto_list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        return super().form_valid(form)

@login_required
def producto_inactivar(request, id):
    model = Producto.objects.filter(pk=id).first()
        
    if request.method == 'GET':
        if model.estado ==True:
            model.estado = False
            messages.success(request, 'Producto inactivado')
        else:
            model.estado = True
            messages.success(request, 'Producto inactivado')
        model.save()
    return redirect('producto_list')
    