from rest_framework import serializers

from reviews.models import Review, Comment


class ReviewSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    title = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    class Meta:
        field = '__all__'
        models = Review


class CommentSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    review = serializers.SlugRelatedField(
        read_only=True,
        slug_field='text',
    )
    text = serializers.SlugRelatedField(
        read_only=True,
        slug_field='text'
    )

    class Meta:
        field = '__all__'
        models = Comment
