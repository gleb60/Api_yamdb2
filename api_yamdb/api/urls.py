<<<<<<< HEAD
from api.views import (
    CommentViewSet,
    ReviewViewSet,
    TitleViewSet,
    CategoryViewSet,
    GenreViewSet
)
from django.urls import include, path
from rest_framework.routers import DefaultRouter

v1_router = DefaultRouter()

v1_router.register('titles', TitleViewSet, basename='titles')
v1_router.register('categories', CategoryViewSet, basename='categories')
v1_router.register('genres', GenreViewSet, basename='genres')
v1_router.register(r'titles/(?P<title_id>\d+)/reviews',
                   ReviewViewSet, basename='reviews')
v1_router.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)'
                   r'/comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
=======
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet

router_v1 = DefaultRouter()
router_v1.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls))
>>>>>>> master
]
