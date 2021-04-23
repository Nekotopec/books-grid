import factory
from django.utils.timezone import make_aware
from . import models
from factory.django import DjangoModelFactory
import factory.fuzzy
import pytz
from datetime import datetime


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
    date_of_finishing = factory.fuzzy.FuzzyDateTime(
        datetime(1500, 1, 1, tzinfo=pytz.UTC),
        datetime.now(tz=pytz.UTC)
    )
