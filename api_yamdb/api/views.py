from rest_framework import viewsets, generics
from reviews.models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
