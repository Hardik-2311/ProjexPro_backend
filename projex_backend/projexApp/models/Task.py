from django.db import models
from projexApp.models import Project


class Task(models.Model):
    Task_name = models.CharField(max_length=150, unique=True)
    created_time = models.DateTimeField(auto_now_add=True)
    project_id = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="tasks"
    )
    time_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"task: {self.Task_name}, in project: {self.project_id.project_name}"
