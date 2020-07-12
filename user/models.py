from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import pre_save
from django.utils.text import slugify
from transliterate import translit
from django.urls import reverse

class User(AbstractUser, models.Model):
    Image = models.ImageField(null=True, blank=True)
    Level = models.PositiveIntegerField(default=0)
    Information = models.CharField(max_length=1024)
    Friends = models.ManyToManyField('self', blank=True, null=True)

    Slug = models.SlugField(blank=True)

def pre_save_slug(sender, instance, *args, **kwargs):
    if not instance.Slug:
        slug = slugify(translit(str(instance.username), 'ru', reversed=True))
        instance.Slug = slug

pre_save.connect(pre_save_slug, sender=(User))



