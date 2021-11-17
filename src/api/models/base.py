from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class StateBaseModel(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        abstract = True
