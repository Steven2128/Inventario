from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

from .models import Proveedor, ComprasEnc, ComprasDet
from .forms import ProveedorForm

class ProveedorView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'cmp.view_proveedor'
    model = Proveedor
    template_name = 'cmp/proveedor_list.html'
    context_object_name = 'obj'


class ProveedorNew(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'cmp.add_proveedor'
    model = Proveedor
    template_name = 'cmp/proveedor_form.html'
    form_class = ProveedorForm
    success_url = reverse_lazy('proveedor_list')

    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)


class ProveedorEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'cmp.change_proveedor'
    model = Proveedor
    template_name = 'cmp/proveedor_form.html'
    form_class = ProveedorForm
    success_url = reverse_lazy('proveedor_list')

    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        return super().form_valid(form)


@login_required
@permission_required('cmp.change_proveedor')
def proveedor_inactivar(request, id):
    model = Proveedor.objects.filter(pk=id).first()
        
    if request.method == 'GET':
        if model.estado ==True:
            model.estado = False
        else:
            model.estado = True
        model.save()
    return redirect('proveedor_list')


class ComprasView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = ComprasEnc
    template_name = 'cmp/compras_list.html'
    context_object_name = 'obj'
    permission_required = 'cmp.view_comprasenc'

