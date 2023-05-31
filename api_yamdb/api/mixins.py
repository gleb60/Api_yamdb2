"""Тут находятся кастомные ViewSet"""
from rest_framework import mixins, viewsets


class CreateDestroyListViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """Этот ViewSet используется для управления жанрами и категориями"""
    pass
