from django.shortcuts import render, redirect
from rest_framework.viewsets import ModelViewSet
from .api.serializer import article_serializer

from .models import article
from django.views.generic import View
from .utils import get_object, get_objects

from .forms import new_article_form
from django.utils import timezone
from django.utils.timezone import localdate

class all_articles(get_objects, View):
    model = article
    template = 'articles/all_articles_page.html'

class article_detail(ModelViewSet):
    model = article
    serializer_class = article_serializer

    def get_queryset(self):
        queryset = article.objects.get_nearby(Slug = self.request.slug)
        return queryset

def add_new(request):
    if request.method == "POST":
        form = new_article_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.Author = request.user
            post.DateAdded = localdate()
            post.DateTimeAdded = timezone.now()
            post.save()
            return redirect('/articles/')
    else:
        form = new_article_form()
    return render(request, 'articles/add_new_page.html', {'form': form})
