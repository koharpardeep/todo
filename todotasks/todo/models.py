from django.db import models

TODO_CHOICES = ((1, 'todo'), (2, 'in_progress'), (3, 'done'))
DEFAULT_TODO_CHOICE = 1


class TodoDetails(models.Model):

    state = models.IntegerField(choices=TODO_CHOICES, default=DEFAULT_TODO_CHOICE)
    due_date = models.DateField()
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)