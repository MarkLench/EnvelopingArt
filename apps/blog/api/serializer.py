from rest_framework.serializers import ModelSerializer
from apps.blog.models import post

class article_serializer(ModelSerializer):
    class Meta:
        model = post
#       fields = ['Title', 'Author', 'Body', 'Date_added',
#        'Date_time_added', 'Likes', 'Dislikes', 'Slug']
