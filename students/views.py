from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import ListModelMixin,\
    RetrieveModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin

from students.models import Student, Course
from students.serializers import StudentSerializer, CourseSerializer


# Create your views here.



class StudentViewSet(
                        ListModelMixin,
                        CreateModelMixin,
                        RetrieveModelMixin,
                        DestroyModelMixin,
                        UpdateModelMixin,
                        GenericViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['age', 'grade']
    search_fields = ['age', 'grade']


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['post'])
    def add_student(self, request, pk=None):
        course = self.get_object()
        student_id = request.data.get('student_id')
        try:
            student = Student.objects.get(id=student_id)
            course.students.add(student)
            return Response({'status': 'student added to course'})
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=404)




