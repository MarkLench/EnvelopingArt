from django.db import models
from user.models import User
from django.utils import timezone
from django.utils.timezone import localdate

from django.db.models.signals import pre_save
from django.utils.text import slugify

def upload_location(instance, filename, **kwargs):
    file_path = 'Publications/{author_id}/{title}-{filename}'.format(
        author_id=str(instance.Author.id), title=str(instance.Title), filename=filename
    )
    return file_path

class article_comment(models.Model):
    Author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles_comment_author')
    AdminComment = models.BooleanField(default=False)
    Body = models.CharField(max_length=512)
    Parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    Likes = models.PositiveIntegerField(default=0)
    Dislikes = models.PositiveIntegerField(default=0)

    DateAdded = models.DateField(default=localdate())
    DateTimeAdded = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.Body

class article(models.Model):
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=120)
    Thesis = models.CharField(max_length=255, null=True, blank=True)
    Body = models.TextField()
    Slug = models.SlugField(blank=True)
    Image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    Parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    Likes = models.PositiveIntegerField(default=0)
    Dislikes = models.PositiveIntegerField(default=0)

    DateAdded = models.DateField(default=localdate())
    DateTimeAdded = models.DateTimeField(default=timezone.now())

    Comments = models.ManyToManyField(article_comment, null=True, blank=True)

    def __str__(self):
        return self.Title

class article_favorite(models.Model):
    Title = models.CharField(max_length=120, blank=True, null=True)
    Favorite = models.ManyToManyField(article, null=True, blank=True)
