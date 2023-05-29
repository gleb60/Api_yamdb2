from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=256)
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
    rating = models.IntegerField(null=True, default=None)
    description = models.TextField(null=True)
    genre = models.ManyToManyField(Genre,
                                   through='GenreTitle',
                                   related_name='titles',)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True)

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.genre} {self.title}'


class Review(models.Model):

    title = models.ForeignKey(
        'Title',
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение',
        null=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор'
    )
    text = models.TextField(
        verbose_name='Отзыв',
        help_text='Напишите ваш отзыв'
    )
    score = models.PositiveSmallIntegerField(
        verbose_name='Рейтинг',
        validators=[
            MinValueValidator(1, 'Минимальное значение 1'),
            MaxValueValidator(10, 'Максимальное значение 10')
        ]
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )

    def __str__(self) -> str:
        return self.text[:20]

    class Meta:
        ordering = ('pub_date', )
        # constraints = [
        #     models.UniqueConstraint(
        #         fields=['title', 'author'],
        #         name='unique_review'
        #     )
        # ]
        verbose_name = 'Комментарий к произведению',
        verbose_name_plural = 'Комментарии к произведениям'
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='unique_review'
            ),
        ]


class Comment(models.Model):

    review = models.ForeignKey(
        'Review',
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв',
        unique=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор',
    )
    text = models.TextField(
        verbose_name='Комментарий',
        help_text='write your comment'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )

    class Meta:
        ordering = ('pub_date',)
        constraints = [
            models.UniqueConstraint(
                fields=['review', 'text'],
                name='unique_comment'
            )
        ]
        verbose_name = 'Комментарий к отзыву',
        verbose_name_plural = 'Комментарии к отзыву'
