from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer
from .models import Book
from .permissions import OnlySafeMethodsOrAdmin


# Create your views here.


class BookModelViewSet(ModelViewSet):
    """
       API endpoint that allows books to be viewed or edited.
    """
    permission_classes = [OnlySafeMethodsOrAdmin]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
