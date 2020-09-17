from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('courses', views.CourseView)
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
