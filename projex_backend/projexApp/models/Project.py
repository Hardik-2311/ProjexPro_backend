from django.db import models
from User import User


class Project(models.Model):
    project_name = models.CharField(max_length=125, unique=True)
    description = models.CharField(max_length=300, null=True)
    wiki = models.CharField(max_length=150, default="IMG PROJECT")
    created_time = models.DateTimeField(auto_now_add=True)
    project_members = models.ManyToManyField(User)
    creator = models.ForeignKey(
        User, related_name="project_created", on_delete=models.SET_NULL, null=True
    )


def is_member(self, username):
    return self.project_members.filter(username=username).exists()
