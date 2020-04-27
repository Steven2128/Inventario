from django.urls import path
from . import views

urlpatterns = [
    path('Clientes/', views.ClienteView.as_view(), name="cliente_list"),
]