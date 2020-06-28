from django.shortcuts import render

from .models import article
from django.views.generic import View
from .utils import DetailMixin


def all_articles(request):
    return render(request, 'articles/all_articles_page.html')



class articleDetailPage(DetailMixin, View):
    model = article
    template = 'articles/all_articles_page.html'
