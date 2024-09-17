from django.urls import path
from . import views

urlpatterns = [
    path('logs', views.Logs , name="logs"),
    path('movement', views.Movement , name="movement"),
]