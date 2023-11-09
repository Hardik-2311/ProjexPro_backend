from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  username=models.CharField(max_length=255,unique=True,primary_key=True)  
  name=models.CharField(max_length=255,null=True)
  year=models.IntegerField(null=True)
  email=models.EmailField(max_length=255,null=True)
  enrolment_no=models.CharField(max_length=8)
  is_Member=models.BooleanField(default=True)
  profile_pic=models.ImageField(upload_to='user_profile_pics/',null=True,blank=True)
  class Meta:
    verbose_name_plural='Users'
  def __str__(self):
    return f"{self.username}"