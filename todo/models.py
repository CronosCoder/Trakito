from django.db import models
from core.models import BaseModel


class Todo(BaseModel):
    name = models.CharField(max_length=500)
    description = models.TextField()
    deadline = models.DateTimeField()
    finish_time = models.DateTimeField(null=True,blank=True)

    class Meta:
        db_table = "todo_Todo"
