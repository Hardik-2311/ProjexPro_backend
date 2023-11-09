from django.db import models
from User import User
project_name=models.CharField(max_length=125,unique=True)
description=models.CharField(max_length=300,null=True)
wiki=models.CharField(max_length=150,default="IMG PROJECT")
created_time=models.DateTimeField(auto_now_add=True)
project_members=models.ManyToManyField(User)
is_private=models.BooleanField(default=False)
project_logo=models.ImageField(upload_to='project_logo/')
creator=models.ForeignKey(User,related_name="project_created",on_delete=models.SET_NULL,null=True)