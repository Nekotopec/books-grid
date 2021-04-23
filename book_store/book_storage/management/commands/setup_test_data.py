import random
from typing import List
from django.db import transaction
from django.core.management.base import BaseCommand


from book_storage.models import Author, Book
from book_storage.factories import AuthorFactory, BookFactory

NUM_AUTHORS = 50
NUM_BOOKS = 1000


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self._delete_old_data(self, *args, **kwargs)
        authors = self._create_authors(*args, **kwargs)
        self._create_books(authors, *args, **kwargs)

    @transaction.atomic
    def _delete_old_data(self, *args, **kwargs):
        """Delete old data"""
        self.stdout.write("Deleting old data...")
        models = [Author, Book]
        for m in models:
            m.objects.all().delete()

    @transaction.atomic
    def _create_authors(self, *args, **kwargs) -> List:
        """Create test data of authors."""
        self.stdout.write("Creating authors data...")
        authors = []
        for _ in range(NUM_AUTHORS):
            author = AuthorFactory()
            authors.append(author)
        return authors

    @transaction.atomic
    def _create_books(self, authors, *args, **kwargs):
        """Create test data of books."""
        self.stdout.write("Creating books data...")
        for _ in range(NUM_BOOKS):
            author = random.choice(authors)
            BookFactory(author=author)
