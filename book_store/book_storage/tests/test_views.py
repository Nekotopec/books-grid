import json

import pytest
from django.test.client import Client
from rest_framework.permissions import AllowAny
from book.settings import REST_FRAMEWORK


from book_storage.views import BookModelViewSet

# Skip decorator.

without_login = pytest.mark.skipif(
    AllowAny in BookModelViewSet.permission_classes,
    reason='Permission classes are disabled.'
)


class TestBookModelViewSet:
    BOOK_DATA = {
        "title": "Test_title",
        "year": "2021",
        "number_of_pages": 1,
        "author": {
            "first_name": "First_name",
            "last_name": "Last_name"
        },
        "number_of_books": 3
    }

    def test_get_books(
            self,
            client: Client,
            create_books,
    ):
        """Test getting of book list."""

        response = client.get('/api/books/')
        books = create_books
        data = response.json()
        assert len(books) == len(data['results'])

    def test_one_receive_book(
            self,
            client: Client,
            create_books,
    ):
        """Test receiving details of one book."""

        response = client.get('/api/books/1/')
        books = create_books
        data = response.json()
        assert books[0].title == data['title']

    @without_login
    def test_bad_deleting_book(
            self,
            client: Client,
            create_books,
    ):
        """Test deleting of the book by non-admin user."""

        response = self._delete_request(client)
        assert response.status_code == 403 or response.status_code == 401

    def test_good_deleting(
            self,
            admin_client: Client,
            create_books,
            token_header
    ):
        """Test deleting of the book by admin user."""

        response = self._delete_request(admin_client, token_header)
        assert response.status_code == 204

    def _delete_request(self, client: Client, headers=None):
        """Make delete request with current client."""

        return client.delete('/api/books/1/', headers=headers)

    def test_patching(
            self,
            admin_client: Client,
            create_books,
            token_header
    ):
        """Test patching of information about the book by admin user."""

        response = self._patch_request(admin_client, token_header)
        response_data = response.json()
        assert response.status_code == 200
        assert response_data['title'] == self.BOOK_DATA['title']
        assert response_data['author']['full_name'] == ' '.join(
            self.BOOK_DATA['author'].values()
        )

    @without_login
    def test_bad_patching(
            self,
            client: Client,
            create_books
    ):
        """Test patching of information about the book by non-admin user."""

        response = self._patch_request(client)
        assert response.status_code == 403 or response.status_code == 401

    def _patch_request(self, client, headers=None):
        return client.patch('/api/books/1/',
                            data=json.dumps(self.BOOK_DATA),
                            content_type='application/json',
                            headers=headers
                            )

    def test_good_posting_book(
            self,
            admin_client: Client,
            token_header
    ):
        """Test posting information about the book by admin user."""

        response = self._post_request(admin_client, token_header)
        response_data = response.json()
        assert response.status_code == 201
        assert response_data['title'] == self.BOOK_DATA['title']
        assert response_data['author']['full_name'] == ' '.join(
            self.BOOK_DATA['author'].values()
        )

    @without_login
    def test_bad_posting_book(
            self,
            client: Client,
    ):
        """Test posting information about the book by non-admin user."""

        response = self._post_request(client)
        assert response.status_code == 403 or response.status_code == 401

    def _post_request(self, client: Client, headers=None):
        """Make post request with current client."""

        return client.post('/api/books/',
                           data=json.dumps(self.BOOK_DATA),
                           content_type='application/json',
                           **headers)
