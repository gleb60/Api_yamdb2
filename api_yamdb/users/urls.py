from django.urls import include, path
from rest_framework import routers

from .views import RegistrationView, UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path('v1/auth/signup/', RegistrationView.as_view(), name='registration'),
    path('v1/auth/token/', include('djoser.urls')),
    path('v1', include(router.urls)),
]
