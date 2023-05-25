from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from rest_framework import status, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import User
from .permissions import IsAdminOrSuperuser
from .serializers import (
    UserRegistrationSerializer, UserSerializer, TokenSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrSuperuser,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RegistrationView(CreateAPIView):
    """Регистрация пользователя"""
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        email = serializer.validated_data.get('email')
        user, created = User.objects.get_or_create(
            username=username,
            email=email
        )
        confirmation_code = default_token_generator.make_token(user)
        send_mail(
            'Код подтверждения почты.',
            f'Здратвсвуйте, {user.username}!'
            f'\nВаш код подтверждения: {confirmation_code}.',
            'from@example.com',
            [email],
            fail_silently=False,
        )
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

class GetJwtToken(CreateAPIView):
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

