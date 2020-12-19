from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    pass

class Page(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pages')
    code = models.TextField(blank=False)