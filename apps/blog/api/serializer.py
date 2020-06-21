from rest_framework.serializers import ModelSerializer
from articles.models import article

class PostSerializer(ModelSerializer):
    class Meta:
        model = article
#        fields = ['Title', 'Author', 'Thesis', 'Content', 'Image', 'DateAdded',
#        'DateTimeAdded', 'Categories', 'Likes', 'Dislikes', 'Slug']
