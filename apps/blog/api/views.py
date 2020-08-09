from apps.blog.models import post
from .serializer import article_serializer

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

class PostsView(viewsets.ModelViewSet):
    queryset = post.objects.all()
    serializer_class = article_serializer

@api_view(['GET'])
def PostViewDetail(request, slug):
    try:
        post = post.objects.get(Slug=slug)
    except post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = article_serializer(post)
        return Response(serializer.data)