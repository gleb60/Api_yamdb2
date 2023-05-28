from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .validators import validate_username


ROLES = (
    ('settings.ADMIN', 'Администратор'),
    ('settings.MODERATOR', 'Модератор'),
    ('settings.USER', 'Пользователь')
)


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        help_text=(_(
            'Обязательное. 150 символов и менее.'
            'Буквы, цифры и @/./+/-/_ только.')
        ),
        validators=[validate_username],
        error_messages={
            'unique': _("Пользователь с таким username уже существует."),
        },
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
        help_text=(_(
            'Обязательное. Например "to1@example.com".')
        ),
    )
    first_name = models.CharField(
        max_length=150,
        blank=True
    )
    last_name = models.CharField(
        max_length=150,
        blank=True
    )
    bio = models.TextField(
        'Биография',
        blank=True
    )
    role = models.CharField(
        'Права доступа',
        max_length=20,
        choices=ROLES,
        default=settings.USER
    )
    confirmation_code = models.CharField(
        'Код подтверждения',
        max_length=256,
        blank=True
    )

    @property
    def is_admin(self):
        return self.role == settings.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == settings.MODERATOR

    class Meta:
        ordering = ['username']
        constraints = [
            models.UniqueConstraint(
                fields=['email', 'username'],
                name='Только один пользователь на email.'
            )
        ]

    def __str__(self):
        return self.username
