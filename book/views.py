from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import BookSerializer,CategorySerializer,AuthorSerializer
from .models import Book,Category,Author

# Create your views here.
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
