from django.db import models
from core.models import BaseModel
from todo.constants import Priority


class Todo(BaseModel):
    name = models.CharField(max_length=500)
    description = models.TextField()
    deadline = models.DateTimeField()
    priority = models.CharField("Priority",max_length=20,choices=Priority.choices, default=Priority.LOW)
    finish_time = models.DateTimeField(null=True,blank=True)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name="todo", null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user} - {self.name}"

    class Meta:
        db_table = "todo_Todo"
