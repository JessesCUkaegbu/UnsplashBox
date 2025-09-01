# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    unsplash_id = models.CharField(max_length=100, unique=True)
    url = models.URLField()
    description = models.TextField(blank=True)
    # Add other fields as needed

class Collection(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.ManyToManyField(Image, related_name='collections')