from rest_framework import serializers

from .models import Book, Author


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'lastName', 'middle_name', 'dateOfBirth']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.SlugRelatedField(slug_field='name', queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        if data['genre'] == 'Fiction' and Book.objects.filter(title=data['title'], author=data['author']).exists():
            raise serializers.ValidationError("Книга с таким заголовком и автором уже существует.")
        elif data['genre'] == 'Textbook' and Book.objects.filter(title=data['title'], author=data['author'],
                                                                 publisher=data['publisher']).exists():
            raise serializers.ValidationError("Учебник с таким же названием, автором и издательством уже существует.")
        return data
