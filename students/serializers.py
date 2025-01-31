from rest_framework import serializers
from .models import Student, Course

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='students-detail')
    courses = serializers.HyperlinkedRelatedField(view_name='courses-detail', many=True, read_only=True)
    class Meta:
        model = Student
        fields = ['url', 'id','first_name', 'last_name', 'age', 'grade', 'courses']




class CourseSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='courses-detail')
    students = serializers.HyperlinkedRelatedField(view_name='students-detail', many=True, read_only=True)
    class Meta:
        model = Course
        fields = '__all__'

