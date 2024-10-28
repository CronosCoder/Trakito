from django.db import models
from core.models import BaseModel
from todo.constants import Priority


class Todo(BaseModel):
    name = models.CharField(max_length=500)
    description = models.TextField()
    deadline = models.DateTimeField()
    priority = models.CharField("Priority",max_length=20,choices=Priority.choices, default=Priority.LOW)
    finish_time = models.DateTimeField(null=True,blank=True)

    class Meta:
        db_table = "todo_Todo"
