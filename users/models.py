from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(('email address'), unique=True)
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=30, blank=True)
    user_name = models.CharField(('username'), max_length=40, blank=True)
    date_joined = models.DateTimeField(('date joined'), auto_now_add=True)
    amount_donated = models.PositiveIntegerField(default=0)
    number_of_posts = models.PositiveIntegerField(default=0)
    status = models.CharField(('status'), max_length=20, default='Member')