from . import views
from django.urls import path

from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register('posts', views.PostsView)
urlpatterns = [
    path('posts/<slug>', views.PostViewDetail, name="PostViewDetail")
]

urlpatterns += router.urls
