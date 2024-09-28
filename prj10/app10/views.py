from django.shortcuts import render

from app10.models import Course, Student 

from django.views import generic 
class StudentListView(generic.ListView): 
    model=Student
    template_name="student_list.html" 
 
class StudentDetailView(generic.DetailView): 
    model=Student
    template_name="student_detail.html" 

 