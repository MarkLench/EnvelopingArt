from django.views.generic import View
from django.shortcuts import render, get_object_or_404

class page_view(View):
    template = ''

    def get(self, request):
        return render(request, self.template)

class page_context_view(View):
    template = None
    model = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, Slug=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})