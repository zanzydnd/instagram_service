from django.db import models

from api.models import BaseModel


class ExtraData(BaseModel):
    data = models.JSONField()
    name = models.CharField(max_length=100)
    comments = models.TextField()

    class Meta:
        db_table = 'extra_data'
