
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buytickets/', include('tickets.urls')),
    path('userdata/', include('lettory_api.urls')),
]
