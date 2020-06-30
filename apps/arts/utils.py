from django.shortcuts import render, get_object_or_404

from .models import *

class DetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, Slug=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})
