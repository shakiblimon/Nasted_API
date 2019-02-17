from rest_framework.serializers import ModelSerializer

from demo.models import Author, Book, Edition


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name','last_name')

class BookSerializer(ModelSerializer):
    model = Book
    class Meta:
        fields = ('id', 'author', 'title')


class EditionSerializer(ModelSerializer):
    model = Edition
    class Meta:
        fields = ('id', 'boook', 'year')
