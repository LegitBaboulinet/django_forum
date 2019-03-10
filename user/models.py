from django.db import models
from datetime import datetime


class User(models.Model):
    username = models.CharField(null=False, unique=True, max_length=25)
    hash = models.CharField(null=False, max_length=100)
    salt = models.CharField(null=False, max_length=40)
    email = models.EmailField(null=True, max_length=75)
    registerDate = models.DateField(null=False, default=datetime.now().date())
