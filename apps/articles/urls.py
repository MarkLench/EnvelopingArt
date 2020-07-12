from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_articles.as_view(), name="all_articles"),
    path('api', include('apps.articles.api.urls')),
]