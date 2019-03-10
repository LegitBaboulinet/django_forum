from django.db import models
from datetime import datetime

from user.models import User


class Post(models.Model):
    title = models.CharField(null=False, max_length=250)
    content = models.TextField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    postDateTime = models.DateTimeField(null=False, default=datetime.now())
