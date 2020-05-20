from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser

from .managers import CustomUserManager

# Create your models here.
class CustomUser(AbstractBaseUser):
    """
        User Data Table, Customized from the default django user table
    """
    normal_user = 'U'
    supplier = 'S'
    role_choices = [
        (normal_user, 'User'),
        (supplier, 'Supplier'),
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=1, choices=role_choices, default=normal_user, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.last_name

    def get_username(self):
        return self.email
