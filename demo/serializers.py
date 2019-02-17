from rest_framework.serializers import ModelSerializer

from demo.models import Author, Book


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        field = ('id', 'first_name','last_name')

class BookSerializer(ModelSerializer):
    model = Book
    class Meta:
        field = ('id', 'name', 'author')


