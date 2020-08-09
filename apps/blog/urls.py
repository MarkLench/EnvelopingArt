from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_posts.as_view(), name="all_posts"),
    path('api', include('apps.blog.api.urls')),
]
