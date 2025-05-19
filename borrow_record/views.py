from django.shortcuts import render
from .serializer import BorrowBookSerializer
from rest_framework.viewsets import ModelViewSet
from .models import BorrowRecord
# Create your views here.
class BorrowBookViewSet(ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowBookSerializer