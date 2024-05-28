from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/reservation/', views.create_reservation, name='create_reservation'),
]
