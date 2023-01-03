from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from users.manager import userManager
# Create your models here.


class Users(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=254)
    name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    # Setting Field
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    # user manager
    objects = userManager()

    class Meta:
        abstract = False
