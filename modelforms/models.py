#models.py File

from django.db import models


class Post(models.Model):
    email= models.CharField(max_length=300, unique=True)
    # content= models.TextField()