from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, TemplateView, UpdateView

from .forms import ProfileForm, ProfileUpdateForm
from .models import Profile

from django.contrib import messages

from .models import Profile

from django.contrib.auth.models import User
from bases.forms import ProfileForm, ProfileUpdateForm
from django.urls import reverse_lazy

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