from rest_framework import serializers
from .models import BorrowRecord

class BorrowBookSerializer(serializers.ModelSerializer):
    member_username = serializers.SerializerMethodField(method_name='get_member_username')
    book_title = serializers.SerializerMethodField(method_name='get_book_title')
    class Meta:
        model = BorrowRecord
        fields = ['id','member_username','book_title','borrow_date','due_date']
        
    def get_member_username(self,user):
        return user.member.username
    
    def get_book_title(self,obj):
        return obj.book.title