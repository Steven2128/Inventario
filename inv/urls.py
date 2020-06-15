from django.urls import path
from django.urls import reverse_lazy
from . import views
from .models import Categoria
urlpatterns = [
    #Categorías CRUD
    path('categorias/', views.CategoriaView.as_view(), name="categoria_list"),
    path('categorias/new', views.CategoriaNew.as_view(), name="categoria_new"),
    path('categorias/edit/<int:pk>', views.CategoriaEdit.as_view(), name="categoria_edit"),
    path('categorias/delete/<int:pk>', views.CategoriaDel.as_view(), name="categoria_del"),
    #Subcategorías CRUD
    path('subcategorias/', views.SubCategoriaView.as_view(), name="subcategoria_list"),
    path('subcategorias/new', views.SubCategoriaNew.as_view(), name="subcategoria_new"),
    path('subcategorias/edit/<int:pk>', views.SubCategoriaEdit.as_view(), name="subcategoria_edit"),
    path('subcategorias/delete/<int:pk>', views.SubCategoriaDel.as_view(), name="subcategoria_del"),
    #Marcas CRUD
    path('marcas/', views.MarcaView.as_view(), name="marca_list"),
    path('marcas/new', views.MarcaNew.as_view(), name="marca_new"),
    path('marcas/edit/<int:pk>', views.MarcaEdit.as_view(), name="marca_edit"),
    path('marcas/inactivar/<int:id>', views.marca_inactivar, name="marca_inactivar"),
    #Unidad de medidas CRUD
    path('um/', views.UnidadMedidaView.as_view(), name="um_list"),
    path('um/new', views.UnidadMedidaNew.as_view(), name="um_new"),
    path('um/edit/<int:pk>', views.UnidadMedidaEdit.as_view(), name="um_edit"),
    path('um/inactivar/<int:id>', views.u_m_inactivar, name="um_inactivar"),
    #Productos CRUD
    path('productos/', views.ProductoView.as_view(), name="producto_list"),
    path('productos/new', views.ProductoNew.as_view(), name="producto_new"),
    path('productos/edit/<int:pk>', views.ProductoEdit.as_view(), name="producto_edit"),
    path('productos/inactivar/<int:id>', views.producto_inactivar, name="producto_inactivar"),
    path('productos/json', views.get_all_products, name="productos_json"),
    path('productos_factura/json', views.products_factura, name="productos_factura_json"),
    
]