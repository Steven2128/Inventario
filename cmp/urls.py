from django.urls import path
from . import views
from .reportes import reporte_compras, imprimir_compra

urlpatterns = [
    #Proveedores CRUD
    path('proveedores/', views.ProveedorView.as_view(), name='proveedor_list'),
    path('proveedores/new', views.ProveedorNew.as_view(), name='proveedor_new'),
    path('proveedores/edit/<int:pk>', views.ProveedorEdit.as_view(), name='proveedor_edit'),
    path('proveedores/inactivar/<int:id>', views.proveedor_inactivar, name='proveedor_inactivar'),
    #Compras CRUD
    path('compras/', views.ComprasView.as_view(), name='compras_list'),
    path('compras/new', views.compras, name='compras_new'),
    path('compras/edit/<int:compra_id>', views.compras, name='compras_edit'),
    path('compras/<int:compra_id>/delete/<int:pk>', views.CompraDetDel.as_view(), name='compras_del'),
    #Reportes de compras
    path('compras/listado', reporte_compras, name='compras_print_all'),
    path('compras/<int:compra_id>/imprimir', imprimir_compra, name='compras_print_one'),
]