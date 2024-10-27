from core.services import BaseService
from todo.models import Todo


class TodoService(BaseService):
    model_class= Todo
    