from rest_framework import serializers

from api.models import Task, TaskType, TaskResult


class TaskSerializer(serializers.ModelSerializer):
    task_id = serializers.PrimaryKeyRelatedField(source='id', read_only=True)
    task_type_id = serializers.PrimaryKeyRelatedField(source='task_type', queryset=TaskType.objects.all())

    class Meta:
        model = Task
        fields = ['task_id', 'task_type_id', 'data', 'priority', 'fields', 'status']
        read_only_fields = ['task_id', 'status']


class TaskResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskResult
        fields = ['task', 'link', 'comment']
        read_only_fields = ['task', 'link', 'comment']