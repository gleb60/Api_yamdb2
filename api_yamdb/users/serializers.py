import re

from rest_framework import serializers

from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Создание пользователя при регистрации."""

    email = serializers.EmailField(
        max_length=254,
        required=True,
        allow_null=False,
        allow_blank=False,
    )
    username = serializers.CharField(
        max_length=150,
        required=True,
        allow_null=False,
        allow_blank=False,
    )

    class Meta:
        model = User
        fields = ('username', 'email')

    def validate(self, data):
        data = super().validate(data)
        pattern = r'^[\w.@+-]+$'
        email = data.get('email')
        username = data.get('username')
        if (not User.objects.filter(email=email, username=username).exists()
                and any((User.objects.filter(email=email).exists(),
                         User.objects.filter(username=username).exists()))):
            raise serializers.ValidationError('Имя или почта заняты.')

        if not re.match(pattern, username) or username == 'me':
            raise serializers.ValidationError('Неверный формат username')

        return data


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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('first_name', 'last_name', 'username', 'bio', 'email',
                  'role')
        model = User
