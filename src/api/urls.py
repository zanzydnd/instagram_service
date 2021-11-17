from django.urls import include, path
from rest_framework import routers

from api.views import TaskViewSet, TaskResultViewSet, TaskResultDetail

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'results', TaskResultViewSet)


urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('result/<int:task_id>/', TaskResultDetail.as_view())
]
