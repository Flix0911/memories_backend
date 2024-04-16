from django.db import models

# Create your models here.

class GoodMemory(models.Model):
    weather = models.CharField(max_length=150)
    comment = models.CharField(max_length=1000)
    attendents = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    season = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    date= models.DateField()
    image = models.ImageField()
    
class BadMemory(models.Model):
    weather = models.CharField(max_length=150)
    comment = models.CharField(max_length=1000)
    attendents = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    season = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    date= models.DateField()
    image = models.ImageField()
    
class Image(models.Model):
    image = models.ImageField()
