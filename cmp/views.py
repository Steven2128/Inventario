from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy

import datetime
from django.http import HttpResponse

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

from .models import Proveedor, ComprasEnc, ComprasDet
from .forms import ProveedorForm, ComprasEncForm
from inv.models import Producto

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


@login_required
@permission_required('cmp.change_comprasenc')
def compras(request, compra_id=None):
    template_name = 'cmp/compras.html'
    prod = Producto.objects.filter(estado=True)
    form_compras = {}
    contexto = {}

    if request.method == 'GET':
        form_compras = ComprasEncForm()
        enc = ComprasEnc.objects.filter(pk=compra_id).first()

        if enc:
            det = ComprasDet.objects.filter(compras=enc)
            fecha_compra = datetime.date.isoformat(enc.fecha_compra)
            fecha_factura = datetime.date.isoformat(enc.fecha_factura)

            e = {
                'fecha_compra': fecha_compra,
                'proveedor': enc.proveedor,
                'observacion': enc.observacion,
                'no_factura': enc.no_factura,
                'fecha_factura': fecha_factura,
                'sub_total': enc.sub_total,
                'descuento': enc.descuento,
                'total': enc.total
            }

            form_compras = ComprasEncForm(e)
        else:
            det = None

        contexto = {'productos': prod, 'encabezado': enc, 'detalle': det, 'form_enc': form_compras}

        return render(request, template_name, contexto)