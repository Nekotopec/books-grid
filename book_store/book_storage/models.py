from datetime import date

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Author(models.Model):
    """Model of author."""

    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, db_index=True)


class Book(models.Model):
    """Model of book."""

    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    number_of_pages = models.PositiveIntegerField()
    number_of_books = models.PositiveIntegerField()
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(date.today().year)
        ])

    def check_if_in_stock(self):
        return self.number_of_books > 0
