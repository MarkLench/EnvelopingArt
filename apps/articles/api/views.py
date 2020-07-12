from apps.articles.models import article
from .serializer import article_serializer

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

class PostsView(viewsets.ModelViewSet):
    queryset = article.objects.all()
    serializer_class = article_serializer

@api_view(['GET'])
def PostViewDetail(request, slug):
    try:
        article = article.objects.get(Slug=slug)
    except article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = article_serializer(article)
        return Response(serializer.data)
