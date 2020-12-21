from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('apps.pages.urls')),
    path('', include('apps.vatsim.urls')),

    path('admin/', admin.site.urls),
]
