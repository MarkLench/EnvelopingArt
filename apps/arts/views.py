from django.shortcuts import render

from .models import art
from django.views.generic import View
from .utils import DetailMixin


def all_arts(request):
    return render(request, 'arts/all_arts_page.html')



class articleDetailPage(DetailMixin, View):
    model = art
    template = 'arts/all_arts_page.html'
