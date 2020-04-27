from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bases.urls')),
    path('inv/', include('inv.urls')),
    path('cmp/', include('cmp.urls')),
    path('factura/', include('factura.urls')),
]
