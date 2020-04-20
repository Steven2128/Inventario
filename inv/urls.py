from django.urls import path
from django.urls import reverse_lazy
from . import views
from .models import Categoria
urlpatterns = [
    #Categorías CRUD
    path('categorias/', views.CategoriaView.as_view(), name="categoria_list"),
    path('categorias/new', views.CategoriaNew.as_view(model=Categoria, success_url=reverse_lazy('categoria_list')), name="categoria_new"),
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
]