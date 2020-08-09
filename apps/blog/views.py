from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .api.serializer import article_serializer

from .models import post
from django.views.generic import View
from .utils import get_object, get_objects


class all_posts(get_objects, View):
    model = post
    template = 'blog/all_posts_page.html'

class post_detail(ModelViewSet):
    model = post
    serializer_class = article_serializer

    def get_queryset(self):
        queryset = post.objects.get_nearby(Slug = self.request.slug)
        return queryset