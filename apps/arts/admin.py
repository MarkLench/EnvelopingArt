from django.contrib import admin
from .models import art, art_comment, art_favorite

admin.site.register(art)
admin.site.register(art_comment)
admin.site.register(art_favorite)
