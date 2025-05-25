from django.shortcuts import render
from .serializer import BorrowBookSerializer
from rest_framework.viewsets import ModelViewSet
from .models import BorrowRecord
from drf_yasg.utils import swagger_auto_schema
# Create your views here.
class BorrowBookViewSet(ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowBookSerializer
    
    
    #JUST FOR SWAGGER DOCUMENTATION
    @swagger_auto_schema(
        operation_summary="List all borrow records",
        operation_description="Returns a list of all borrow records with member username and book title.",
        tags=["Borrow Records"]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a borrow record",
        operation_description="Returns a specific borrow record by ID.",
        tags=["Borrow Records"]
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a borrow record",
        operation_description="Create a new borrow record by providing member and book IDs. Admin only.",
        tags=["Borrow Records"]
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a borrow record",
        operation_description="Update an existing borrow record by ID. Admin only.",
        tags=["Borrow Records"]
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partially update a borrow record",
        operation_description="Partially update a borrow record. Admin only.",
        tags=["Borrow Records"]
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a borrow record",
        operation_description="Delete a borrow record by ID. Admin only.",
        tags=["Borrow Records"]
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)