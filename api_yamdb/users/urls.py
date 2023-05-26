from django.urls import include, path
from rest_framework import routers

from .views import RegistrationView, UserViewSet, GetJwtToken

app_name = 'users'

router = routers.DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path('auth/signup/', RegistrationView.as_view(), name='signup'),
    path('auth/token/', GetJwtToken.as_view(), name='token'),
    path('', include(router.urls)),
]
