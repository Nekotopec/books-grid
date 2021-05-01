from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Book, Author


class AuthorSerializer(ModelSerializer):
    full_name = serializers.SerializerMethodField(read_only=True)
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'full_name']
        read_only_fields = ['full_name', 'id']

    def get_full_name(self, obj):
        """Returns full name of author."""

        if obj.first_name is None:
            return obj.last_name
        return ' '.join([obj.first_name, obj.last_name])

    def create(self, validated_data):
        try:
            author = Author.objects.get(last_name=validated_data['last_name'],
                                        first_name=validated_data['first_name'])
        except Author.DoesNotExist:
            author = Author.objects.create(
                last_name=validated_data['last_name'],
                first_name=validated_data['first_name']
            )
        return author


class BookSerializer(ModelSerializer):
    author = AuthorSerializer(required=False)
    author_fullname = serializers.CharField(required=False, write_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'year', 'author',
                  'number_of_pages', 'author_fullname',
                  'number_of_books']

    def create(self, validated_data):
        author_data = validated_data.pop('author', None)
        if author_data:
            author = AuthorSerializer().create(author_data)
        else:
            author = extjs_author_crutch(validated_data)

        book = Book.objects.create(author=author,
                                   **validated_data)
        return book

    def update(self, instance, validated_data):
        author_data = validated_data.pop('author', None)
        if author_data:
            author = AuthorSerializer().create(author_data)
            validated_data['author_id'] = author.id
        elif validated_data.get('author_fullname'):
            author = extjs_author_crutch(validated_data)
            validated_data['author_id'] = author.id

        book = super().update(instance, validated_data)
        return book


def extjs_author_crutch(data):
    """Returns author instance.
    I made it cause I cant find how edit nested models in grid in extjs."""
    fullname = data.pop('author_fullname')
    split_name = fullname.split(' ')
    if len(split_name) > 1:
        first_name = split_name[0]
        last_name = split_name[1]
    else:
        first_name = None
        last_name = split_name[0]
    author = Author.objects.create(
        first_name=first_name,
        last_name=last_name,
    )
    return author
