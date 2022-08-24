from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.


class Quotes(models.Model):
    quote = models.TextField(unique=True, null=False)
    author = models.CharField(max_length=255, unique=True, null=False)
    genre = models.CharField(max_length=255, null=False)
