from rest_framework.pagination import LimitOffsetPagination
from api.models import Genre, Category, Title
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import (GenreSerializer,
                          CategorySerializer,
                          TitleSerializer,
                          TitleWriteSerializer)
from .permissions import IsAdminOrReadOnly

class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = LimitOffsetPagination
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    filterset_fields = ('category', 'genre', 'name', 'year',)
    search_fields = ('titles__name',)

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitleSerializer
        return TitleWriteSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminOrReadOnly]
