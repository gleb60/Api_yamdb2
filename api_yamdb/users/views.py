from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny

from .models import User
from .serializers import UserSerializer, UserRegistrationSerializer
from .permissions import IsAdminOrSuperuser


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrSuperuser]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class RegistrationView(CreateAPIView):
    """Регистрация пользователя"""
    permission_classes = [AllowAny, ]
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        pass