from django.db import models

from django.contrib.postgres.fields import ArrayField
from api.models import SocialNetworkType, BaseModel, BloggerState, Task


class SocialNetworkUser(BaseModel):
    social_id = models.CharField(max_length=100)
    social_network_type = models.ForeignKey(SocialNetworkType, null=True, on_delete=models.SET_NULL)
    parsed_at = models.DateTimeField()
    account_created_date = models.DateField(null=True)
    birth_date = models.DateField(null=True)
    email = models.EmailField(null=True)
    social_login = models.CharField(max_length=100, null=True)
    full_name = models.CharField(max_length=150, null=True)
    additional_content = models.TextField(null=True)
    phone = models.CharField(max_length=20, null=True)
    subscribed_ids = ArrayField(
        models.CharField(max_length=100), null=True
    )
    followers = models.BigIntegerField(null=True)
    following = models.BigIntegerField(null=True)
    contents = models.BigIntegerField(null=True)
    task = models.ForeignKey(Task, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'social_network_user'


class SocialNetworkContent(models.Model):
    content_id = models.CharField(max_length=100)
    photo = models.TextField(null=True)
    user = models.ForeignKey(SocialNetworkUser, on_delete=models.CASCADE)
    likes = models.IntegerField(null=True)
    comments = models.IntegerField(null=True)
    task = models.ForeignKey(Task, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'social_network_content'


class Blogger(BaseModel):
    login = models.CharField(max_length=150, null=True)
    social_id = models.CharField(max_length=100)
    social_network_type = models.ForeignKey(SocialNetworkType, null=True, on_delete=models.SET_NULL)
    subscribers_count = models.BigIntegerField(null=True)
    content_count = models.BigIntegerField(null=True)
    following = models.BigIntegerField(null=True)
    categories = ArrayField(
        models.CharField(max_length=50), null=True
    )
    age = models.IntegerField(null=True)
    state = models.ForeignKey(BloggerState, null=True, on_delete=models.SET_NULL)
    another_socials = ArrayField(
        models.CharField(max_length=100), null=True
    )
    another_links = ArrayField(
        models.CharField(max_length=250), null=True
    )
    task = models.ForeignKey(Task, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'blogger'
