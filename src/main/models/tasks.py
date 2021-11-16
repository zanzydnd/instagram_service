from django.contrib.postgres.fields import ArrayField
from django.db import models

from main.models import BaseModel, TaskType, TaskStatus


class Task(BaseModel):
    task_type = models.ForeignKey(TaskType, null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey(TaskStatus, null=True, on_delete=models.SET_NULL)
    data = models.JSONField()
    priority = models.IntegerField()
    fields = ArrayField(
        models.CharField(max_length=50)
    )

    class Meta:
        db_table = 'task'


class TaskResult(BaseModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    link = models.FileField()
    comment = models.TextField(null=True)

    class Meta:
        db_table = 'task_result'
