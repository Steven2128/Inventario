from django.urls import path
from . import views

urlpatterns = [
    path('Clientes/', views.ClienteView.as_view(), name="cliente_list"),
    path('Clientes/new', views.ClienteNew.as_view(), name="cliente_new"),
    path('Clientes/edit/<int:pk>', views.ClienteEdit.as_view(), name="cliente_edit"),
]