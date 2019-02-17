from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from demo.models import Author, Book
from demo.serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class BookviewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
