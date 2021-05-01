from datetime import date

import factory.fuzzy
from factory.django import DjangoModelFactory

from . import models


class AuthorFactory(DjangoModelFactory):
    class Meta:
        model = models.Author

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class BookFactory(DjangoModelFactory):
    class Meta:
        model = models.Book

    title = factory.Faker('sentence', nb_words=4)
    number_of_pages = factory.Faker('pyint', min_value=0, max_value=1000)
    number_of_books = factory.Faker('pyint', min_value=0, max_value=400)
    year = factory.fuzzy.FuzzyInteger(low=0, high=date.today().year)
