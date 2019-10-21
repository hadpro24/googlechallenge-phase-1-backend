from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=30)
    film = models.ForeignKey('Film', on_delete=models.CASCADE, related_name='languages')

    def __str__(self):
        return self.name

class Award(models.Model):
    name = models.CharField(max_length=255)
    received_it = models.DateField()
    film = models.ForeignKey('Film', on_delete=models.CASCADE, related_name='awards')

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=100)
    film = models.ForeignKey('Film', on_delete=models.CASCADE, related_name='directors')

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=100)
    film = models.ForeignKey('Film', on_delete=models.CASCADE, related_name='actors')

    def __str__(self):
        return self.name

class Writer(models.Model):
    name = models.CharField(max_length=100)
    film = models.ForeignKey('Film', on_delete=models.CASCADE, related_name='writers')

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)
    film = models.ForeignKey('Film', on_delete=models.CASCADE, related_name='genres')

    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=100)
    released = models.DateField()
    description = models.TextField()
    runtime = models.DurationField()
    country = models.CharField(max_length=150)
    rated = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to='films/')

    def __str__(self):
        return self.title
