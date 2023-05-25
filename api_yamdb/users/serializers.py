from django.core.validators import EmailValidator
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
        write_only=True,
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
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ('username', 'email')

    def create(self, validated_data):
        return User.objects.creare(**validated_data)

    @staticmethod
    def validate_username(username):
        if username == 'me':
            raise serializers.ValidationError(
                "Имя 'me' зарезервировано."
            )
        return username


class TokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=150,
        required=True,
        allow_null=False,
        allow_blank=False,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')
