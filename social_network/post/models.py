from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author_name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post")
    creation_date = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0, editable=False)
