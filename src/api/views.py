from django.http import Http404
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet
from tasks import start_parse
from api.models import Task, TaskResult
from api.serializers import TaskSerializer, TaskResultSerializer


class TaskViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        items = request.data['data']['items']
        start_parse.delay(response.data['task_id'], items)

        return response


class TaskResultDetail(APIView):
    """
    Retrieve, update or delete a task_result instance.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, task_id):
        try:
            return TaskResult.objects.get(task_id=task_id)
        except TaskResult.DoesNotExist:
            raise Http404

    def get(self, request, task_id, format=None):
        task_result = self.get_object(task_id)
        serializer = TaskResultSerializer(task_result)
        return Response(serializer.data)


class TaskResultViewSet(ReadOnlyModelViewSet):
    serializer_class = TaskResultSerializer
    queryset = TaskResult.objects.all()
    permission_classes = [IsAuthenticated]
