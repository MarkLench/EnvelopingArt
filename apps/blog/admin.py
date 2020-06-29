from django.contrib import admin
from .models import post, post_comment

admin.site.register(post)
admin.site.register(post_comment)
