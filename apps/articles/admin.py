from django.contrib import admin
from .models import article, article_comment, article_favorite

admin.site.register(article)
admin.site.register(article_comment)
admin.site.register(article_favorite)
