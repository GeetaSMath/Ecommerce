from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    address = models.TextField(max_length=500)
    phone_number = models.IntegerField(default=10)

