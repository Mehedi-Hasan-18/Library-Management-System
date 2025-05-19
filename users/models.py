from django.contrib.auth.models import AbstractUser
from django.db import models

class Member(AbstractUser):
    email = models.EmailField(unique=True)
    membership_date = models.DateField(auto_now_add=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True) 

    def __str__(self):
        return self.username
    