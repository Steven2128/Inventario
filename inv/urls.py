from django.urls import path
from . import views

urlpatterns = [
    path('categorias/', views.CategoriaView.as_view(), name="categoria_list")
]