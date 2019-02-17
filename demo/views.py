from django.shortcuts import render

# Create your views here.
from rest_framework.utils.model_meta import _get_pk
from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin

from demo.models import Author, Book, Edition
from demo.serializers import AuthorSerializer, BookSerializer, EditionSerializer


class AuthorViewSet( NestedViewSetMixin, ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class BookViewSet(NestedViewSetMixin,ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.filter(author={1})


class EditionViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = EditionSerializer
    queryset = Edition.objects.filter(book__author={1}, book={2})


