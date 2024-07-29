from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='Account', null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    def __str__(self):
        return self.get_full_name()



