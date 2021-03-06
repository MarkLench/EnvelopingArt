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

class post_comment(models.Model):
    Author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_comment_author')
    Admin_comment = models.BooleanField(default=False)
    Body = models.CharField(max_length=512)
    Parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    Likes = models.PositiveIntegerField(default=0)
    Dislikes = models.PositiveIntegerField(default=0)

    Date_added = models.DateField(default=localdate())
    Date_time_added = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.Body

class post(models.Model):
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=120)
    Body = models.TextField()
    Slug = models.SlugField(blank=True)
    Likes = models.PositiveIntegerField(default=0)
    Dislikes = models.PositiveIntegerField(default=0)

    Date_added = models.DateField(default=localdate())
    Date_time_added = models.DateTimeField(default=timezone.now())

    Comments = models.ManyToManyField(post_comment, null=True, blank=True)

    def __str__(self):
        return self.Title


def pre_save_slug(sender, instance, *args, **kwargs):
    if not instance.Slug:
        slug = slugify(translit(str(instance.Title), 'ru', reversed=True))
        instance.Slug = slug

pre_save.connect(pre_save_slug, sender=(post))
