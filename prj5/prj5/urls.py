
from django.contrib import admin
from django.urls import path, re_path 
from app5.views import find_mode 

urlpatterns = [ 
path('admin/', admin.site.urls), 
path('find_mode/<str:listofnum>', find_mode), 
]
