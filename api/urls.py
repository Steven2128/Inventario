from django.urls import path
from . import views

urlpatterns = [
    path('v1/productos/', views.ProductoList.as_view(), name='producto_list_api'),
    path('v1/productos/<str:codigo>', views.ProductoDetalle.as_view(), name='producto_detalle'),
]