from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #as it is default, no need to fill model 
    date_posted = models.DateTimeField(default=timezone.now)
    #if author deleted, post will also be deleted 
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

