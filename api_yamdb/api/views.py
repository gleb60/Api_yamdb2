from rest_framework.pagination import LimitOffsetPagination
from api.models import Genre, Category, Title
from rest_framework import viewsets
from rest_framework import filters
from .serializers import (GenreSerializer, CategorySerializer, TitleSerializer,)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = []
    pagination_class = LimitOffsetPagination


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^name')


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = []
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^name')
