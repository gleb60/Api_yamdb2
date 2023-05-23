from django.db import models
from users.models import User

# Create your models here.
class Reviews(models.Model):


# The model of comments to reviews.
class Comment(models.Model):

    reviews = models.ForeignKey(
        'Review',
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='review',
        blank=True,
        null=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Author',
    )
    text = models.TextField(
        verbose_name='comments',
        help_text='write your comment'
    )


    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Comment',
        verbose_name_plural = 'Comments'