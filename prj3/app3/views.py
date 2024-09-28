from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template

def create_table_of_squares(request,s,n):
    result=""
    for i in range(1,n+1):
        result="<p>"+str(s)+"*"+str(i)+"="+str((s*i))+"</p"
        return HttpResponse(result)
    

# Create your views here.
