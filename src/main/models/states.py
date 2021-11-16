from main.models import StateBaseModel


class SocialNetworkType(StateBaseModel):

    class Meta:
        db_table = 'social_network_type'


class BloggerState(StateBaseModel):

    class Meta:
        db_table = 'blogger_state'


class TaskStatus(StateBaseModel):

    class Meta:
        db_table = 'task_status'


class TaskType(StateBaseModel):

    class Meta:
        db_table = 'task_type'
