"""Тут находятся кастомные пермишены"""
from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """Ограничивает доступ к редактированию жанров, категорий, произведений"""
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or (not request.user.is_anonymous and request.user.is_admin))


class IsAdminModeratorOwnerOrReadOnly(permissions.BasePermission):
    """Ограничивает доступ к редактированию комментариев и ревью"""
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_admin
                or request.user.is_moderator
                or obj.author == request.user)

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)
