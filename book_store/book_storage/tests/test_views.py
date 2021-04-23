from django.test.client import Client
import json


class TestBookModelViewSet:
    BOOK_DATA = {
        "title": "Test_title",
        "date_of_finishing": "2021-04-23T14:17:01.464Z",
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

    def test_bad_deleting_book(
            self,
            client: Client,
            create_books,
    ):
        """Test deleting of the book by non-admin user."""

        response = self._delete_request(client)
        assert response.status_code == 403

    def test_good_deleting(
            self,
            admin_client: Client,
            create_books
    ):
        """Test deleting of the book by admin user."""

        response = self._delete_request(admin_client)
        assert response.status_code == 204

    def _delete_request(self, client: Client):
        """Make delete request with current client."""

        return client.delete('/api/books/1/')

    def test_patching(
            self,
            admin_client: Client,
            create_books
    ):
        """Test patching of information about the book by admin user."""

        response = self._patch_request(admin_client)
        response_data = response.json()
        assert response.status_code == 200
        assert response_data['title'] == self.BOOK_DATA['title']
        assert response_data['author']['full_name'] == ' '.join(
            self.BOOK_DATA['author'].values()
        )

    def test_bad_patching(
            self,
            client: Client,
            create_books
    ):
        """Test patching of information about the book by non-admin user."""

        response = self._patch_request(client)
        assert response.status_code == 403

    def _patch_request(self, client):
        return client.patch('/api/books/1/',
                            data=json.dumps(self.BOOK_DATA),
                            content_type='application/json')

    def test_good_posting_book(
            self,
            admin_client: Client,
    ):
        """Test posting information about the book by admin user."""

        response = self._post_request(admin_client)
        response_data = response.json()
        assert response.status_code == 201
        assert response_data['title'] == self.BOOK_DATA['title']
        assert response_data['author']['full_name'] == ' '.join(
            self.BOOK_DATA['author'].values()
        )

    def test_bad_posting_book(
            self,
            client: Client,
    ):
        """Test posting information about the book by non-admin user."""

        response = self._post_request(client)
        assert response.status_code == 403

    def _post_request(self, client: Client):
        """Make post request with current client."""

        return client.post('/api/books/',
                           data=json.dumps(self.BOOK_DATA),
                           content_type='application/json')