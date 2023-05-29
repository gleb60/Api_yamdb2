import datetime as dt

from django.db.models import Avg
from django.forms import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from reviews.models import Category, Comment, Genre, Review, Title


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        lookup_field = 'slug'
        fields = ('name', 'slug')

    def validate_slug(self, value):
        if self.instance and self.instance.slug == value:
            return value
        if Category.objects.filter(slug=value).exists():
            raise serializers.ValidationError('Slug must be unique.')
        return value


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        lookup_field = 'slug'
        fields = ('name', 'slug')

    def validate_slug(self, value):
        if self.instance and self.instance.slug == value:
            return value
        if Genre.objects.filter(slug=value).exists():
            raise serializers.ValidationError('Slug must be unique.')
        return value


class TitleGetSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    genre = GenreSerializer(many=True)
    category = CategorySerializer()

    

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'rating', 'description', 'genre',
                  'category')
        
    def get_rating(self, obj):
        rating = obj.reviews.aggregate(Avg("score")).get("score__avg")
        return rating

    def validate_year(self, value):
        """Проверяет, что год выпуска раньше текущего"""
        year = dt.date.today().year
        if (value < year):
            raise serializers.ValidationError(
                'Дата не может быть позднее текущей'
            )
        return value


class TitleWriteSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        slug_field='slug', many=True, queryset=Genre.objects.all()
    )
    category = serializers.SlugRelatedField(
        slug_field='slug', queryset=Category.objects.all()
    )

    class Meta:
        model = Title
        fields = ('__all__')


class ReviewSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    title = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    def validate(self, data):
        request = self.context['request']
        author = request.user
        title_id = self.context['view'].kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)
        if request.method == 'POST':
            if Review.objects.filter(title=title, author=author).exists():
                raise ValidationError('Вы не можете добавить более'
                                      'одного отзыва на произведение')
        return data

    class Meta:
        fields = '__all__'
        model = Review


class CommentSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    review = serializers.SlugRelatedField(
        read_only=True,
        slug_field='text'
    )

    class Meta:
        fields = '__all__'
        model = Comment
