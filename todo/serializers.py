from rest_framework import serializers
from todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id","name", "description", "deadline", "is_active", "priority"]


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id","name", "deadline", "is_active", "priority"]


class TodoUpdateStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id","is_active"]


class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"