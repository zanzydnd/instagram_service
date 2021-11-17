from api.models import Task
from instagram_service.celery import app


@app.task
def start_parse(task_id, items):
    task = Task.objects.get(id=task_id)

    #parser
