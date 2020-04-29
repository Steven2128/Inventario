from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView


class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'base/home.html'


class VistaBaseCreate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    success_message = 'Registro agregado exitosamente!'

    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)


class VistaBaseEdit(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        return super().form_valid(form)