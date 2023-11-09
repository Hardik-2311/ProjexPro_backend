from django.db import models
from .Goal import Goal
from .User import User
from django.utils import timezone
class feedback(models.Model):

    content = models.TextField()

    goal_id = models.ForeignKey(
       Goal,
        primary_key = False,
        on_delete = models.CASCADE,
    )

    commentor = models.ForeignKey(
        User, 
        primary_key = False,
        on_delete = models.CASCADE,
        related_name = 'commented_cards',
    )

    timestamp = models.DateTimeField(default = timezone.now)

    is_edited = models.BooleanField(default = False)
    
    def __str__(self):
        return f"{self.content} *BY* {self.commentor.username}"