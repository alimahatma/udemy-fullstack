from .models import Book
from rest_framework import serializers



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title', 'description','price','published', 'is_published']