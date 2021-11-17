from django.http import Http404
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet

from api.models import Task
from api.serializers import TaskSerializer


class TaskViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        items = request.data['data']['items']
        start_parse.delay(response.data['task_id'], items)

        return response

