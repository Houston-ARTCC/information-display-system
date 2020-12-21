from django.contrib import admin
from django.urls import path

from flights import views as flights


urlpatterns = [
    # Flights
    path('flights/', flights.view_enroute_strips),
    path('flights/add/', flights.add_flight),
    # Django Admin
    path('admin/', admin.site.urls),
]
