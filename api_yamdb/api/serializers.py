from rest_framework import serializers
import datetime as dt
from reviews.models import Title, Category, Genre, GenreTitle


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
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
        fields = ('name', 'slug')

    def validate_slug(self, value):
        if self.instance and self.instance.slug == value:
            return value
        if Genre.objects.filter(slug=value).exists():
            raise serializers.ValidationError('Slug must be unique.')
        return value


class TitleGetSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer()

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'rating', 'description', 'genre',
                  'category')

    def validate_year(self, value):
        """Проверяет, что год выпуска раньше текущего"""
        year = dt.date.today().year
        if (value < year):
            raise serializers.ValidationError('Ошибка. Дата позднее текущей.')
        return value


class TitleWriteSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        slug_field='slug', many=True, queryset=Genre.objects.all()
    )
    category = serializers.SlugRelatedField(
        slug_field='slug', queryset=Category.objects.all()
    )

    def create(self, validated_data):
        if 'genre' not in self.initial_data:
            title = Title.objects.create(**validated_data)
            return title
        else:
            genre = validated_data.pop('genre')
            title = Title.objects.create(**validated_data)
            for genre in genre:
                current_genre, status = Genre.objects.get_or_create(
                    **genre)
                GenreTitle.objects.create(
                    genre=current_genre, title=title)
            return title
