from django.db import models

from helpers.models import TimestampModel

# Create your models here.

class Comment(TimestampModel):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE)