from django.db import models
from book.models import Book
from users.models import Member

# Create your models here.
class BorrowRecord(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='borrow')
    member = models.ForeignKey(Member,on_delete=models.CASCADE,related_name='borrow')
    borrow_date = models.DateTimeField()
    return_date = models.DateTimeField()
    due_date = models.DateTimeField()
    
    def __str__(self):
        return f"{self.member.username} borrowed '{self.book.title}' on {self.borrow_date.strftime('%Y-%m-%d')}"