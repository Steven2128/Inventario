from django.urls import path
from django.urls import reverse_lazy
from . import views
from .models import Categoria
urlpatterns = [
    path('categorias/', views.CategoriaView.as_view(), name="categoria_list"),
    path('categorias/new', views.categoriaNew.as_view(model=Categoria, success_url=reverse_lazy('categoria_list')), name="categoria_new"),
]