from django_filters import rest_framework as filters
from .models import Todo


class TodoFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    description = filters.CharFilter(field_name="description", lookup_expr="icontains")
    deadline = filters.DateTimeFilter(field_name="deadline", lookup_expr="lte")
    priority = filters.CharFilter(field_name="priority", lookup_expr="icontains")
    is_active = filters.BooleanFilter(field_name="is_active")

    class Meta:
        model = Todo
        fields = ["name", "description", "deadline", "priority", 'is_active']
