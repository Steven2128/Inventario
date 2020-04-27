from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Cliente
from .forms import ClienteForm

class ClienteView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'factura.view_cliente'
    model = Cliente
    template_name = 'cmp/cliente_list.html'
    context_object_name = 'obj'
