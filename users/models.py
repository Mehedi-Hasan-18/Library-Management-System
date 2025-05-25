from django.contrib.auth.models import AbstractUser
from django.db import models
from users.managers import MemberManager

class Member(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    membership_date = models.DateField(auto_now_add=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MemberManager()

    def __str__(self):
        return self.email
    