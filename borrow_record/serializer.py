from rest_framework import serializers
from .models import BorrowRecord

class BorrowBookSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField(method_name='get_member_email')
    book_title = serializers.SerializerMethodField(method_name='get_book_title')
    class Meta:
        model = BorrowRecord
        fields = ['id','email','book_title','borrow_date','due_date','return_date']
        
    def get_member_email(self,user):
        return user.member.email
    
    def get_book_title(self,obj):
        return obj.book.title