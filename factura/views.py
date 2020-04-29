from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from bases.views import VistaBaseCreate, VistaBaseEdit

from .models import Cliente
from .forms import ClienteForm

class ClienteView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'factura.view_cliente'
    model = Cliente
    template_name = 'cmp/cliente_list.html'
    context_object_name = 'obj'


class ClienteNew(VistaBaseCreate):
    permission_required = 'factura.add_cliente'
    model = Cliente
    template_name = 'factura/cliente_form.html'
    form_class = ClienteForm
    success_url = reverse_lazy('cliente_list')


class ClienteEdit(VistaBaseEdit):
    permission_required = 'factura.change_cliente'
    model = Cliente
    template_name = 'factura/cliente_form.html'
    form_class = ClienteForm
    success_url = reverse_lazy('cliente_list')