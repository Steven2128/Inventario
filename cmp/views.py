from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json

from .models import Proveedor
from .forms import ProveedorForm

class ProveedorView(LoginRequiredMixin, ListView):
    model = Proveedor
    template_name = 'cmp/proveedor_list.html'
    context_object_name = 'obj'
    login_url = 'login'


class ProveedorNew(LoginRequiredMixin, CreateView):
    model = Proveedor
    template_name = 'cmp/proveedor_form.html'
    form_class = ProveedorForm
    success_url = reverse_lazy('proveedor_list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)


class ProveedorEdit(LoginRequiredMixin, UpdateView):
    model = Proveedor
    template_name = 'cmp/proveedor_form.html'
    form_class = ProveedorForm
    success_url = reverse_lazy('proveedor_list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        return super().form_valid(form)


@login_required
def proveedor_inactivar(request, id):
    model = Proveedor.objects.filter(pk=id).first()
        
    if request.method == 'GET':
        if model.estado ==True:
            model.estado = False
        else:
            model.estado = True
        model.save()
    return redirect('proveedor_list')