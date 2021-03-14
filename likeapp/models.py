from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='like')

    class Meta:
        unique_together = ('user', 'article')
