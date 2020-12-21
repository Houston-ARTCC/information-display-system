from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.auth, name='login'),
    path('logout/', views.deauth, name='logout'),
]
