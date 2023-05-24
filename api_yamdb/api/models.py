from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    name = models.CharField (max_length=256)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=256)
    year = models.IntegerField()
    rating = models.IntegerField(null=True)
    description = models.TextField()
    genre = models.ForeignKey(Genre, 
                              on_delete=models.CASCADE,
                              related_name='titles',
                              )
    category = models.OneToOneField(Category,
                                    on_delete=models.CASCADE,
                                    related_name='titles',)

    def __str__(self):
        return self.name
