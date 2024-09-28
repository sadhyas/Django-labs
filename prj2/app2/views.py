from django.shortcuts import render

def greet(request,user):
    uname=user
    d={'user':user}
    return render(request,'greet',d)

