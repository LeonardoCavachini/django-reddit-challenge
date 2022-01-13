from django.db import models

from helpers.models import TimestampModel

# Create your models here.
class Post(TimestampModel):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    topic = models.ForeignKey('topic.Topic', on_delete=models.CASCADE)