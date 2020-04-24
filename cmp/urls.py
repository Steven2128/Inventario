from django.urls import path
from . import views

urlpatterns = [
    #Proveedores CRUD
    path('proveedores/', views.ProveedorView.as_view(), name='proveedor_list'),
    path('proveedores/new', views.ProveedorNew.as_view(), name='proveedor_new'),
    path('proveedores/edit/<int:pk>', views.ProveedorEdit.as_view(), name='proveedor_edit'),
    path('proveedores/inactivar/<int:id>', views.proveedor_inactivar, name='proveedor_inactivar'),
    #Compras CRUD
    path('compras/', views.ComprasView.as_view(), name='compras_list'),
    path('compras/new', views.compras, name='compras_new'),
]