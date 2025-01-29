from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, CourseViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='students')
router.register(r'courses', CourseViewSet, basename='courses')
urlpatterns = [
    path('', include(router.urls)),
]