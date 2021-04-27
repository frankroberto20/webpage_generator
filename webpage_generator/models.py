from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    pass

class Page(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pages')
    title = models.CharField(max_length=256, blank=False)

class Section(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='sections')
    heading = models.CharField(max_length=256, blank=False)
    content = models.TextField(blank=False)