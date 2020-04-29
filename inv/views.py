from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto
from .forms import CategoriaForm, SubCategoriaForm, MarcaForm, UnidadMedidaForm, ProdutoForm


class CategoriaView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = 'inv.view_categoria'
    model = Categoria
    template_name = 'inv/categoria_list.html'
    context_object_name = 'obj'


class CategoriaNew(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.CreateView):
    permission_required = 'inv.add_categoria'
    template_name = 'inv/categoria_form.html'
    form_class = CategoriaForm
    success_message = 'Categoría creada exitosamente!'
    success_url = reverse_lazy('categoria_list')

    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)


class CategoriaEdit(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    permission_required = 'inv.change_categoria'
    model = Categoria
    template_name = 'inv/categoria_form.html'
    form_class = CategoriaForm
    success_message = 'Categoría actualizada exitosamente!'
    success_url = reverse_lazy('categoria_list')

    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        return super().form_valid(form)


class CategoriaDel(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'inv.delete_categoria'
    model = Categoria
    template_name = 'inv/categoria_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('categoria_list')


class SubCategoriaView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = 'inv.view_subcategoria'
    model = SubCategoria
    template_name = 'inv/subcategoria_list.html'
    context_object_name = 'obj'


class SubCategoriaNew(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.CreateView):
    permission_required = 'inv.add_subcategoria'
    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    success_message = 'Subcategoría creada exitosamente!'
    success_url = reverse_lazy('subcategoria_list')
    form_class = SubCategoriaForm

    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)


class SubCategoriaEdit(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    permission_required = 'inv.change_subcategoria'
    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    form_class = SubCategoriaForm
    success_message = 'Subcategoría actualizada exitosamente!'
    success_url = reverse_lazy('subcategoria_list')

    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        return super().form_valid(form)


class SubCategoriaDel(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'inv.delete_subcategoria'
    model = SubCategoria
    template_name = 'inv/categoria_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('subcategoria_list')


class MarcaView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = 'inv.view_marca'
    model = Marca
    template_name = 'inv/marca_list.html'
    context_object_name = 'obj'


class MarcaNew(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.CreateView):
    permission_required = 'inv.add_marca'
    model = Marca
    template_name = 'inv/marca_form.html'
    form_class = MarcaForm
    success_message = 'Marca creada exitosamente!'
    success_url = reverse_lazy('marca_list')

    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)


class MarcaEdit(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    permission_required = 'inv.change_marca'
    model = Marca
    template_name = 'inv/marca_form.html'
    form_class = MarcaForm
    success_message = 'Marca actualizada exitosamente!'
    success_url = reverse_lazy('marca_list')

    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        return super().form_valid(form)

@login_required
@permission_required('inv.change_marca')
def marca_inactivar(request, id):
    model = Marca.objects.filter(pk=id).first() 
    if request.method == 'GET': 
        if model.estado ==True: 
            model.estado = False
        else: 
            model.estado = True
        model.save()
        
    return redirect('marca_list')


class UnidadMedidaView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = 'inv.view_unidadmedida'
    model = UnidadMedida
    template_name = 'inv/um_list.html'
    context_object_name = 'obj'


class UnidadMedidaNew(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.CreateView):
    permission_required = 'inv.add_unidadmedida'
    template_name = 'inv/um_form.html'
    form_class = UnidadMedidaForm
    success_message = 'Unidad de medida creada exitosamente!'
    success_url = reverse_lazy('um_list')

    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)


class UnidadMedidaEdit(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    permission_required = 'inv.change_unidadmedida'
    model = UnidadMedida
    template_name = 'inv/um_form.html'
    form_class = UnidadMedidaForm
    success_message = 'Unidad de medida actualizada exitosamente!'
    success_url = reverse_lazy('um_list')

    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        return super().form_valid(form)

@login_required
@permission_required('inv.change_unidadmedida')
def u_m_inactivar(request, id):
    model = UnidadMedida.objects.filter(pk=id).first()
        
    if request.method == 'GET':
        if model.estado ==True:
            model.estado = False
        else:
            model.estado = True
        model.save()
    return redirect('um_list')


class ProductoView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = 'inv.view_producto'
    model = Producto
    template_name = 'inv/product_list.html'
    context_object_name = 'obj'


class ProductoNew(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.CreateView):
    permission_required = 'inv.add_producto'
    model = Producto
    template_name = 'inv/producto_form.html'
    form_class = ProdutoForm
    success_message = 'Producto creado exitosamente!'
    success_url = reverse_lazy('producto_list')

    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)


class ProductoEdit(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    permission_required = 'inv.change_producto'
    model = Producto
    template_name = 'inv/producto_form.html'
    form_class = ProdutoForm
    success_message = 'Producto actualizado exitosamente!'
    success_url = reverse_lazy('producto_list')

    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        return super().form_valid(form)

@login_required
@permission_required('inv.change_producto')
def producto_inactivar(request, id):
    model = Producto.objects.filter(pk=id).first()
        
    if request.method == 'GET':
        if model.estado ==True:
            model.estado = False
        else:
            model.estado = True
        model.save()
    return redirect('producto_list')
    