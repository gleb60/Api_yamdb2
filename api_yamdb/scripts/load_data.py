from django.core.management.base import BaseCommand
from reviews.models import Title, Genre, Category, Review, Comment
import csv


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.load_titles()


    def load_titles(self, file_path):
        with open('static/data/titles.csv', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                title = Title()
                title.name = row['name']
                title.year = int(row['year'])
                title.description = row['description']
                title.category = row['category']
                title.genre = row['genre']
                title.save()