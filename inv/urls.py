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
]