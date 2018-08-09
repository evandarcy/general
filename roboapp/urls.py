from django.urls import path

from . import views

urlpatterns = [
    path('arena', views.arena, name='arena'),
]
