import pytest
from book_storage.factories import BookFactory, AuthorFactory
from typing import List
from book_storage import models


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