from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('duels/', views.duels, name='duels'),
    path('arena', views.arena, name='arena'),
    path('ajax/<str:robot1_id>/<str:robot2_id>',views.ajax, name='ajax'),
    path('entry/<int:entry>/<int:id>', views.entry, name='entry'),
    path('ajax',views.ajax, name='ajax'),
]
