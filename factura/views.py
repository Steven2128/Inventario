from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.decorators import login_required, permission_required

from django.core import serializers
from django.http import HttpResponse

from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from bases.views import VistaBaseCreate, VistaBaseEdit

from datetime import datetime

from .models import Cliente, FacturaEnc, FacturaDet
from inv.models import Producto
import inv.views as inv
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


@login_required
@permission_required('cmp.change_cliente')
def cliente_inactivar(request, id):
    model = Cliente.objects.filter(pk=id).first()
        
    if request.method == 'GET':
        if model.estado ==True:
            model.estado = False
        else:
            model.estado = True
        model.save()
    return redirect('cliente_list')


class FacturaView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'factura.view_facturaenc'
    model = FacturaEnc
    template_name = 'factura/factura_list.html'
    context_object_name = 'obj'

@login_required
@permission_required('factura.change_facturaenc')
def facturas(request, id=None):
    template_name = 'factura/factura.html'

    encabezado = {
        'fecha': datetime.today()
    }

    detalle = {}
    clientes = Cliente.objects.filter(estado=True)

    if request.method == 'GET':
        enc = FacturaEnc.objects.filter(pk=id).first()
        if not enc:
            encabezado = {
                'id':0,
                'fecha': datetime.today(),
                'cliente':0,
                'sub_total': 0.00,
                'descuento': 0.00,
                'total': 0.00
            }
            detalle = None
        else:
            encabezado = {
                'id':enc.id,
                'fecha': enc.fecha,
                'cliente':enc.cliente,
                'sub_total': enc.sub_total,
                'descuento': enc.descuento,
                'total': enc.total,
            }
            detalle = FacturaDet.objects.filter(factura=enc)
    contexto = {'enc': encabezado, 'det': detalle, 'clientes': clientes}

    return render(request, template_name, contexto)


class ProductoView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'inv.view_producto'
    model = Producto
    template_name = "factura/buscar_producto.html"
    context_object_name = 'obj'