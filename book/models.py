from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=250)
    biography = models.TextField()
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='book')
    ISBN = models.CharField(max_length=100,unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='book')
    availability = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.title} {self.ISBN}'