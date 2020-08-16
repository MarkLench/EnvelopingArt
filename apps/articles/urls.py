from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_articles.as_view(), name="all_articles"),
    path('add_new/', views.add_new, name="add_new_article"),

    path('api', include('apps.articles.api.urls')),
]