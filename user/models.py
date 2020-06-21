from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser, models.Model):
    Image = models.ImageField(null=True, blank=True)
    Level = models.PositiveIntegerField(default=0)
    Information = models.CharField(max_length=1024)




