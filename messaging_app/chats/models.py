from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import uuid



# Create your models here.
class CustomUser(AbstractBaseUser):
    """
    Custom User Model
    """

    ROLE_CHOICES = (
       ("guest", "Guest" ),
       ("host", "Host"),
       ("admin", "Admin")
    )
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    phone_number = models.CharField(null=False, blank=False)
    role = models.CharField(null=False, 
                            choices=ROLE_CHOICES
                            )
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    first_name = models.CharField(max_length=55, blank=False, null=False)
    last_name = models.CharField(max_length=55, blank=False, null=False)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=55, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self. username