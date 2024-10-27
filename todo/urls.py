from django.urls import path, include
from todo.views import (
    TodoListCreateAPIView,
    TodoRetrieveUpdateAPIView
)

urlpatterns = [
    path("todos/", TodoListCreateAPIView.as_view(), name="todo_list_create"),
    path("todos/<int:id>/", TodoRetrieveUpdateAPIView.as_view(), name="todo_retrieve_update"),
]
