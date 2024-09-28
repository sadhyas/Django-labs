from django.shortcuts import render
from urllib import response
from django.http import HttpResponse
from app11.models import Course
import csv
def construct_csv_from_model(request):
    courses=Course.objects.all()
    response=HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment;filename="courses_data.csv"'
    writer=csv.writer(response)
    writer.writerow(["Course Name","Course Code","Credits"]) 
    for course in courses:
        writer.writerow([course.course_name,course.course_code,course.course_credits])
    return response

 