import re
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username', 'email')
        model = User


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Создание пользователя при регистрации."""

    email = serializers.EmailField(
        max_length=254,
        required=True,
        allow_null=False,
        allow_blank=False,
        validators=[EmailValidator(), UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        max_length=150,
        required=True,
        allow_null=False,
        allow_blank=False,
        validators=[
            UniqueValidator(queryset=User.objects.all()),
        ]
    )

    class Meta:
        model = User
        fields = ('username', 'email')

    @staticmethod
    def validate_username(username):
        if username == 'me':
            raise serializers.ValidationError(
                "Имя 'me' зарезервировано."
            )
        if not re.match(r'^[a-zA-Z][\w+.@+-]{1,150}$', username):
            raise ValidationError(_(f'{username} содержит недопустимые символы!'))
        return username


class TokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=150,
        required=True,
        allow_null=False,
        allow_blank=False,
    )
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')
