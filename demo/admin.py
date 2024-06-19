from django.contrib import admin
from .models import Book, BookNumber

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title','price']
    list_filter = ['published']
    search_fields = ['title']

admin.site.register(BookNumber)

