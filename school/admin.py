from django.contrib import admin

from school.models import Student
from school.models import School
from school.models import Grade

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    pass

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    pass