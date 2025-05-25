from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import BookSerializer,CategorySerializer,AuthorSerializer,BookWriteSerializer
from .models import Book,Category,Author
from api.permission import IsAdminOrReadOnly
from drf_yasg.utils import swagger_auto_schema

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return BookWriteSerializer
        return BookSerializer

    #JUST FOR DOCUMENTATION
    @swagger_auto_schema(
        operation_summary="List all books",
        operation_description="Returns a list of all books with author and category data"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a book",
        operation_description="Get details of a single book"
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=BookWriteSerializer,
        responses={201: BookSerializer},
        operation_summary="Create a book",
        operation_description="Creates a new book. Requires admin access."
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Update a Book",
        operation_description="Updates a Book's information. Admin only.",
        tags=["books"]
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partially update a Book",
        operation_description="Partially updates Book fields. Admin only.",
        tags=["books"]
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a Book",
        operation_description="Deletes a Book. Admin only.",
        tags=["books"]
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    
    #JUST FOR DOCUMENTATION
    @swagger_auto_schema(
        operation_summary="List all categories",
        operation_description="Returns a list of all book categories.",
        tags=["Categories"]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a category",
        operation_description="Returns details of a specific category by ID.",
        tags=["Categories"]
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a category",
        operation_description="Creates a new category. Admin access required.",
        tags=["Categories"]
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a category",
        operation_description="Updates a category's information. Admin only.",
        tags=["Categories"]
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partially update a category",
        operation_description="Partially updates category fields. Admin only.",
        tags=["Categories"]
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a category",
        operation_description="Deletes a category. Admin only.",
        tags=["Categories"]
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    #JUST FOR DOCUMENTATION
    @swagger_auto_schema(
        operation_summary="List all authors",
        operation_description="Returns a list of all authors.",
        tags=["Authors"]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve an author",
        operation_description="Returns details of an author by ID.",
        tags=["Authors"]
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create an author",
        operation_description="Creates a new author. Admin access required.",
        tags=["Authors"]
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update an author",
        operation_description="Updates an author's information. Admin only.",
        tags=["Authors"]
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partially update an author",
        operation_description="Partially updates author fields. Admin only.",
        tags=["Authors"]
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete an author",
        operation_description="Deletes an author. Admin only.",
        tags=["Authors"]
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
