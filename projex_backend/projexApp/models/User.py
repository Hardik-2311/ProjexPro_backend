from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True, primary_key=True)  
    name = models.CharField(max_length=255, null=True)
    year = models.IntegerField(null=True)
    email = models.EmailField(max_length=255, null=True)
    enrolment_no = models.CharField(max_length=8)
    is_Member = models.BooleanField(default=True)
    profile_pic = models.ImageField(upload_to='profile_pic', null=True, blank=True)

    objects = CustomUserManager()

    class Meta:
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"{self.username}"