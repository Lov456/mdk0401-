from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/catalog/', include('catalog.urls')),
    path('api/clients/', include('clients.urls')),
    path('api/orders/', include('orders.urls')),
]