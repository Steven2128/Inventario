from django.urls import path
from . import views

urlpatterns = [
    #Clientes CRUD
    path('clientes/', views.ClienteView.as_view(), name="cliente_list"),
    path('clientes/new', views.ClienteNew.as_view(), name="cliente_new"),
    path('clientes/edit/<int:pk>', views.ClienteEdit.as_view(), name="cliente_edit"),
    path('clientes/estado/<int:id>', views.cliente_inactivar, name="cliente_inactivar"),
    #Facturas CRUD
    path('facturas/', views.FacturaView.as_view(), name="factura_list"),
    path('facturas/new', views.facturas, name="factura_new"),
    path('facturas/edit/<int:id>', views.facturas, name="factura_edit"),
    path('facturas/buscar_producto', views.ProductoView.as_view(), name="factura_producto"),
    path('facturas/borrar_detalle/<int:id>', views.borrar_detalle_factura, name="borrar_detalle"),
]