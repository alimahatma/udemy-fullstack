from rest_framework import viewsets
from .serializers import BookSerializer
# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import View
from .models import Book
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



# class Another(View):
#      book = Book.objects.get(id=2)
#     output = f"We have book: {book.title} book with ID {book.id} <br>"
    
#     # for book in books:
#     #     output += f'{book.id}. We have a Books, The title: {book.title} in DB <br>'
    
#     def get(self, request):
#         return HttpResponse(self.output)

# def first(request): 
#     books = Book.objects.all()
#     return render(request, 'first_temp.html', {'books':books})
 
class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,) 

   