from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .api.serializer import article_serializer

from .models import article
from django.views.generic import View
from .utils import get_object, get_objects


class all_articles(get_objects, View):
    model = article
    template = 'articles/all_articles_page.html'

class article_detail(ModelViewSet):
    model = article
    serializer_class = article_serializer

    def get_queryset(self):
        queryset = article.objects.get_nearby(Slug = self.request.slug)
        return queryset