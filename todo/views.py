from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from todo.services import TodoService
from todo.serializers import (
    TodoSerializer,
    TodoDetailSerializer,
    TodoListSerializer,
    TodoUpdateStatusSerializer
)
from core.paginators import Pagination


class TodoListCreateAPIView(views.APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer
    pagination_class = Pagination
    list_serializer_class = TodoListSerializer
    detail_serializer_class = TodoDetailSerializer
    service_class = TodoService()

    def get(self, request):
        todos = self.service_class.all(user=request.user)
        paginator = self.pagination_class()
        paginated_todos = paginator.paginate_queryset(todos, request)
        response = self.list_serializer_class(paginated_todos, many=True).data
        return paginator.get_paginated_response(response)

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.service_class.create(serializer.validated_data,request=request)
        return Response(self.detail_serializer_class(instance).data,status=status.HTTP_201_CREATED)
    

class TodoRetrieveUpdateAPIView(views.APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer
    list_serializer_class = TodoListSerializer
    detail_serializer_class = TodoDetailSerializer
    update_status_serializer = TodoUpdateStatusSerializer
    service_class = TodoService()

    def get(self, request, *args, **kwargs):
        todo = self.service_class.get(**kwargs)
        response = self.detail_serializer_class(todo)
        return Response(response.data, status=status.HTTP_200_OK)

    def put(self,request, *args, **kwargs):
        todo = self.service_class.get(id=kwargs.get("id"))
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.service_class.update(instance=todo, validated_data=serializer.validated_data,request=request)
        return Response(self.detail_serializer_class(instance).data,status=status.HTTP_200_OK)
    
    


class TodoUpdateStatusAPIView(views.APIView):


    def patch(self, request, *args, **kwargs):
        pass



