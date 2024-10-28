from django.urls import path, include
from .views import *
# from todo.views import (
#     TodoListCreateAPIView,
#     TodoRetrieveUpdateAPIView 
# )

urlpatterns = [
    path("todos/", TodoListCreateAPIView.as_view(), name="todo_list_create"),
    path("todos/<int:id>/", TodoRetrieveUpdateAPIView.as_view(), name="todo_retrieve_update"),
    path("todos/<int:id>/update-status/", TodoUpdateStatusAPIView.as_view(), name="todo_update_status"),
]
