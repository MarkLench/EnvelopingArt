from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_posts.as_view(), name="all_posts"),
    path('add_new/', views.add_new, name="add_new_post"),

    path('api', include('apps.blog.api.urls')),
]
