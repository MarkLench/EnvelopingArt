from django.shortcuts import render

from .models import post
from django.views.generic import View
from .utils import DetailMixin


def all_posts(request):
    return render(request, 'blog/all_posts_page.html')



class articleDetailPage(DetailMixin, View):
    model = post
    template = 'blog/all_posts_page.html'