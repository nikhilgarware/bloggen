from statistics import mode
from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255, unique=True, null=False)
    content = models.TextField()
    created_by = models.CharField(max_length=255, null=False)
    tags = models.CharField(max_length=255)
    published = models.BooleanField(default=False)
    updated_by = models.CharField(max_length=266)
