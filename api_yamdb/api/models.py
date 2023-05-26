from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug


class Genre(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug


class Title(models.Model):
    name = models.CharField(max_length=256)
    year = models.IntegerField()
    rating = models.IntegerField(null=True)
    description = models.TextField(null=True)
# посмотреть achivments
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
