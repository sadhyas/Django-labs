from django.contrib import admin

from app7.models import Course, Student
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['student_usn','student_name','student_sem']
    ordering=('student_usn',)
    search_fields=('student_usn',)
admin.site.register(Course)