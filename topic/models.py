from django.db import models
from django.db.models.deletion import CASCADE

from helpers.models import TimestampModel

# Create your models here.
class Topic(TimestampModel):
    title = models.CharField(max_length=50)
    author = models.ForeignKey('accounts.User', on_delete=CASCADE)
    description = models.CharField(max_length=150)
    URLName = models.SlugField(max_length=100)
