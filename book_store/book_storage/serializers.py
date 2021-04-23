from .models import Book, Author
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class AuthorSerializer(ModelSerializer):
    full_name = serializers.SerializerMethodField(read_only=True)
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'full_name']
        read_only_fields = ['full_name', 'id']

    def get_full_name(self, obj):
        """Returns full name of author."""
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
    author = AuthorSerializer()
    in_stock = serializers.SerializerMethodField()
    year = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'year', 'date_of_finishing',
                  'number_of_pages', 'author', 'in_stock',
                  'number_of_books']
        read_only_fields = ['author_full_name', 'year']
        extra_kwargs = {
            'number_of_books': {'write_only': True},
            'date_of_finishing': {'write_only': True},
        }

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author = AuthorSerializer().create(author_data)

        book = Book.objects.create(author=author,
                                   **validated_data)
        return book

    def update(self, instance, validated_data):
        author_data = validated_data.pop('author')
        author = AuthorSerializer().create(author_data)
        validated_data['author_id'] = author.id
        book = super().update(instance, validated_data)
        return book

    def get_year(self, obj):
        """Get year from date of finishing."""
        return obj.date_of_finishing.year

    def get_in_stock(self, obj):
        """Check if book in stock."""
        return obj.check_if_in_stock()
