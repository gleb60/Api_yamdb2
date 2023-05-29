from django.forms import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import serializers
import datetime as dt
from reviews.models import Comment, Review, Title, Category, Genre
from django.db.models import Avg


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

<<<<<<< HEAD
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
=======
    class Meta:
        field = '__all__'
        models = Review
>>>>>>> e04df430ed800199ed21cbf5afa1a79272ae9e6e


class CommentSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    review = serializers.SlugRelatedField(
        read_only=True,
<<<<<<< HEAD
=======
        slug_field='text',
    )
    text = serializers.SlugRelatedField(
        read_only=True,
>>>>>>> e04df430ed800199ed21cbf5afa1a79272ae9e6e
        slug_field='text'
    )

    class Meta:
<<<<<<< HEAD
        fields = '__all__'
        model = Comment
=======
        field = '__all__'
        models = Comment
>>>>>>> e04df430ed800199ed21cbf5afa1a79272ae9e6e
