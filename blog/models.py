from django.db import models
import datetime
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=60)
    author = models.CharField(max_length=30)
    content = models.TextField(max_length=2000)
    posted = models.DateTimeField('date published')

    def __str__(self):
        return self.title


class Comments(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    commenter = models.CharField(max_length=30)
    email = models.EmailField()
    content = models.TextField(max_length=1000)
    posted = models.DateTimeField('date published')

    def __str__(self):
        return self.commenter
