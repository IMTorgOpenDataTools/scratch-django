from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import ExaminerViewSet

router = DefaultRouter()
router.register(r'users', ExaminerViewSet)

urlpatterns = [
    path('users/', include(router.urls))
]