from django.contrib import admin

# Register your models here.
from .models import Student, Course

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass