from typing import List

import pytest

from book_storage import models
from book_storage.factories import BookFactory, AuthorFactory
from rest_framework.authtoken.models import Token


@pytest.fixture(autouse=True)
def enable_db_access(db):
    pass


@pytest.fixture(scope='function')
def create_books(db) -> List[models.Book]:
    """Create 10 books of one author."""
    author = AuthorFactory()
    books = [BookFactory(author=author) for _ in range(10)]
    yield books
    for book in books:
        book.delete()
    author.delete()


@pytest.fixture(scope='function')
def token_header(db, client, admin_user):
    token = Token.objects.get_or_create(user=admin_user)
    print(token[0])
    headers = {
        'Authorization': f'Token {token[0]}'
    }
    yield headers
