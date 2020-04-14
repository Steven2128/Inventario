from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Categoria
from .forms import CategoriaForm


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