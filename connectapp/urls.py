from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('game/<str:room_name>/', views.game, name='room_name'),
]