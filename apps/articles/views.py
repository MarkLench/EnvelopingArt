from django.shortcuts import render

from .models import article
from django.views.generic import View
from .utils import DetailMixin

"""
def allPostsPage(request):
    return render(request, 'html/AllPostsPage.html')



class articleDetailPage(DetailMixin, View):
    model = article
    template = 'html/PostDetailPage.html'
"""