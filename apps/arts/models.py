from django.db import models
from user.models import User
from django.utils import timezone
from django.utils.timezone import localdate

from django.db.models.signals import pre_save
from django.utils.text import slugify
from transliterate import translit
from django.urls import reverse

def upload_location(instance, filename, **kwargs):
    file_path = 'Publications/{author_id}/{title}-{filename}'.format(
        author_id=str(instance.Author.id), title=str(instance.Title), filename=filename
    )
    return file_path

class art_comment(models.Model):
    Author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='art_comment_author')
    AdminComment = models.BooleanField(default=False)
    Body = models.CharField(max_length=512)
    Parent = models.ForeignKey('self', blank=True, null=True, related_name='child_set', on_delete=models.CASCADE)
    Likes = models.PositiveIntegerField(default=0)
    Dislikes = models.PositiveIntegerField(default=0)

    DateAdded = models.DateField(default=localdate())
    DateTimeAdded = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.Body

class art(models.Model):
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=120, blank=True, null=True)
    Thesis = models.CharField(max_length=512, null=True, blank=True)
    Slug = models.SlugField(blank=True)
    Image = models.ImageField(upload_to=upload_location)
    Likes = models.PositiveIntegerField(default=0)
    Dislikes = models.PositiveIntegerField(default=0)

    DateAdded = models.DateField(default=localdate())
    DateTimeAdded = models.DateTimeField(default=timezone.now())

    Comments = models.ManyToManyField(art_comment, null=True, blank=True)

    def __str__(self):
        return self.Title

class art_favorite(models.Model):
    Title = models.CharField(max_length=120, blank=True, null=True)
    Favorite = models.ManyToManyField(art, null=True, blank=True)


def pre_save_slug(sender, instance, *args, **kwargs):
    if not instance.Slug:
        slug = slugify(translit(str(instance.Title), 'ru', reversed=True))
        instance.Slug = slug

pre_save.connect(pre_save_slug, sender=(art))
pre_save.connect(pre_save_slug, sender=(art_favorite))
