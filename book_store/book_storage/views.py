from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer


# Create your views here.


class BookModelViewSet(ModelViewSet):
    """
       API endpoint that allows books to be viewed or edited.
    """
    # permission_classes = [OnlySafeMethodsOrAdmin]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
