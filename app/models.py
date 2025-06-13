from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


ARTICLE_STATUS = (('draft', 'published'),
                  ('in_progress', 'in progress'),
                  ('published', 'published'))


class UserProfile(AbstractUser):
    pass


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, default="")
    word_count = models.IntegerField()
    twitter_post = models.TextField(blank=True, default="")
    status = models.CharField(max_length=20,
                              choices=ARTICLE_STATUS,
                              default='draft')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
