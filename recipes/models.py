from django.db import models
from django.contrib.postgres.fields import ArrayField
from PIL import Image

class Recipes(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    ingredients = ArrayField(models.CharField(max_length=50, blank=True), default=list)
    def __str__(self):
        return self.name
    image = models.ImageField(upload_to = 'images/', default = 'blank')
