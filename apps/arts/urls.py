from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_arts, name="all_arts"),
]
