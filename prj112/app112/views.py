from django.shortcuts import render
from urllib import response
from django.http import HttpResponse
from app112.models import Course
from reportlab.pdfgen import canvas
def construct_pdf_from_model(request):
    courses=Course.objects.all()
    response=HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment;filename="courses_data.pdf"'
    c=canvas.Canvas(response) 
    c.drawString(70,720,"Course Name")
    c.drawString(170,720,"Course Code")
    c.drawString(270,720,"Credits") 
    y=660
    for course in courses: 
        c.drawString(70,y,course.course_name)
        c.drawString(170,y,course.course_code)
        c.drawString(270,y,str(course.course_credits))
        y=y-60
        c.showPage() 
        c.save()
    return response 