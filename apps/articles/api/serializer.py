from rest_framework.serializers import ModelSerializer
from apps.articles.models import article

class article_serializer(ModelSerializer):
    class Meta:
        model = article
#       fields = ['Title', 'Author', 'Thesis', 'Body', 'Image', 'DateAdded',
#        'DateTimeAdded', 'Category', 'Likes', 'Dislikes', 'Slug']
