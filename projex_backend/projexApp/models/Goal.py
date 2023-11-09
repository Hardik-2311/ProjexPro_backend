from django.db import models
from .User import User
from .Task import Task


class goal(models.Model):
    task_id = models.ForeignKey(
        Task,
        primary_key=False,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=100)
    desc = models.TextField(blank=True)

    creator = models.ForeignKey(
        User,
        primary_key=False,
        on_delete=models.DO_NOTHING,
        related_name="goal_creator",
    )
    assignees = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    due_date = models.DateField(
        auto_now=False,
        auto_now_add=False,
    )

    finished_status = models.BooleanField(default=False)

    def __str__(self):
        return f"goal in {self.task_id} by {self.creator.username}"
