from . import views
from django.urls import path

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('articles', views.PostsView)
urlpatterns = [
    path('articles/<slug>', views.PostViewDetail, name="PostViewDetail")
]

urlpatterns += router.urls
