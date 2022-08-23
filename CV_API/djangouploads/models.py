from django.db import models


class ImageInfo(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')


class Drink(models.Model):
    name = models.CharField(max_length=200)
    # description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/', null=True)
    # def __str__(self):
    #     return self.name + " " + self.description
