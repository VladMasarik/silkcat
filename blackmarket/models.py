from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    image_path = models.CharField(max_length=256)
