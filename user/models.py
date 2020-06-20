from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser, models.Model):
    Image = models.ImageField(null=True, blank=True)

