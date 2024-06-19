from .models import Book, BookNumber
from rest_framework import serializers


class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        fields = ['id','isbn_10','isbn_13']


class BookSerializer(serializers.ModelSerializer):
    #kode ini menghubungkan class BookNumberSerializer ke BookSerializer
    number = BookNumberSerializer(read_only=False)

    class Meta:
        model = Book
        fields = ['id','title', 'description','price','published', 'is_published','number']
        