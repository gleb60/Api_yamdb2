from rest_framework import serializers
import datetime as dt
from api.models import Title, Category, Genre


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'slug')


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'slug')


class TitleSerializer(serializers.ModelSerializer):
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
