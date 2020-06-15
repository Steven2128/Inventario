from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, TemplateView, UpdateView

from .forms import ProfileForm, ProfileUpdateForm
from .models import Profile

from datetime import datetime

from django.contrib import messages

from .models import Profile

from django.contrib.auth.models import User
from bases.forms import ProfileForm, ProfileUpdateForm
from django.urls import reverse_lazy

from django.db.models import Sum, F, FloatField
from inv.models import Producto, SubCategoria
from factura.models import FacturaEnc
from cmp.models import ComprasEnc
from factura.models import Cliente

@login_required
def home(request):
    template_name = 'base/home.html'
    producto = {
        'inventario_neto' : Producto.objects.all().aggregate(total=Sum(F('precio') * F('existencia'), output_field=FloatField())),
        'productos_stock': Producto.objects.all().count()
    }

    ventas = {
        'factura_neto': FacturaEnc.objects.filter(fecha__year=datetime.now().year).aggregate(Sum('total')),
        'facturas_emitidas': FacturaEnc.objects.all().count()
    }

    compras = {
        'compra_neto': ComprasEnc.objects.filter(fecha_factura__year=datetime.now().year).aggregate(Sum('total')),
        'compras_emitidas': ComprasEnc.objects.all().count()
    }
    subcategorias = SubCategoria.objects.all()
    labels_subcategorias = []
    subcategorias_stock = []
    for i in subcategorias:
        labels_subcategorias.append(i.descripcion)
        cant = Producto.objects.filter(subcategoria=i.pk).aggregate(Sum('existencia'))
        cant = cant['existencia__sum']
        subcategorias_stock.append(cant)

    facturas_por_mes = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    compras_por_mes = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']

    for i in range(0, 12):
        factura_por_mes = FacturaEnc.objects.filter(fecha__month=i+1).aggregate(Sum('total'))
        compra_por_mes = ComprasEnc.objects.filter(fecha_factura__month=i+1).aggregate(Sum('total'))
        factura_por_mes = factura_por_mes['total__sum']
        compra_por_mes = compra_por_mes['total__sum']

        if factura_por_mes is None:
            factura_por_mes = 0
        
        if compra_por_mes is None:
            compra_por_mes = 0

        facturas_por_mes[i] = int(factura_por_mes)
        compras_por_mes[i] = int(compra_por_mes)
    print(labels_subcategorias)
    context = {
        'producto': producto,
        'ventas': ventas,
        'compras': compras,
        'clientes': Cliente.objects.all().count(),
        'ventas_mes': facturas_por_mes,
        'compras_mes': compras_por_mes,
        'labels_subcategorias': labels_subcategorias,
        'subcategorias_stock': subcategorias_stock,
        'ahora': datetime.now()
    }
    return render(request, template_name, context)


class VistaBaseCreate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    success_message = 'Registro agregado exitosamente!'

    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)


class VistaBaseEdit(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        return super().form_valid(form)



@login_required
def profile(request):
    if request.method == 'POST':
        user_form = ProfileForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Cuenta actualizada exitosamente!')
            return redirect('profile')

    else:
        user_form = ProfileForm(instance=request.user)
        pro = Profile.objects.filter(user_id=request.user.id)
        if not pro:
            profile = Profile(user=request.user)
            profile.save()
    context = {
        'u_form': user_form,
    }

    return render(request, 'base/profile.html', context)