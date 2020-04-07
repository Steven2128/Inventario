from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'base/home.html'
    login_url = 'login'