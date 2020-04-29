from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.ClienteView.as_view(), name="cliente_list"),
    path('clientes/new', views.ClienteNew.as_view(), name="cliente_new"),
    path('clientes/edit/<int:pk>', views.ClienteEdit.as_view(), name="cliente_edit"),
    path('clientes/estado/<int:id>', views.cliente_inactivar, name="cliente_inactivar"),
]