from django.shortcuts import render, redirect
from rest_framework.viewsets import ModelViewSet
from .api.serializer import article_serializer

from .models import post
from django.views.generic import View
from .utils import get_object, get_objects

from .forms import new_post_form
from django.utils import timezone
from django.utils.timezone import localdate


class all_posts(get_objects, View):
    model = post
    template = 'blog/all_posts_page.html'

class post_detail(ModelViewSet):
    model = post
    serializer_class = article_serializer

    def get_queryset(self):
        queryset = post.objects.get_nearby(Slug = self.request.slug)
        return queryset


def add_new(request):
    if request.method == "POST":
        form = new_post_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.Author = request.user
            post.Date_added = localdate()
            post.Date_time_added = timezone.now()
            post.save()
            return redirect('/blog/')
    else:
        form = new_post_form()
    return render(request, 'blog/add_new_page.html', { 'form' : form })