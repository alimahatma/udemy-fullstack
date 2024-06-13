from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book

class Another(View):
    books = Book.objects.all()
    output = ''
    
    for book in books:
        output += f'{book.id}. We have {book.title} book in DB <br>'
    
    def get(self, request):
        return HttpResponse(self.output)
    
    

def first(request): 
    return HttpResponse("<h1>This The First.</h1>")
