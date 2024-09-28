from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    resp="<h1>Hellow World!!!</h1>"
    return HttpResponse(resp)