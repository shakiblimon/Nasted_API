from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin

from demo.models import Author, Book
from demo.serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class BookviewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
