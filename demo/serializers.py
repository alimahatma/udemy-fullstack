from .models import Book, BookNumber, Character, Author
from rest_framework import serializers


class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        fields = ['id','isbn_10','isbn_13']

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id','name']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author 
        fields = ['id','name','surname']


class BookSerializer(serializers.ModelSerializer):
    #kode ini menghubungkan class BookNumberSerializer ke BookSerializer
    number = BookNumberSerializer(read_only=False)

    #kode ini menghubungkan class CharacterSerializer ke BookSerializer
    characters = CharacterSerializer(many=True)

    #kode ini menghubungkan class AuthorSerializer ke BookSerializer
    authors = AuthorSerializer(many=True) 


    class Meta:
        model = Book
        fields = ['id','title', 'description','price','published', 'is_published','number','characters','authors']


#! ini untuk membuat class BookMini menampilkan separuh informasi yang dibutuhkan
class BookMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title']
        