
from django.contrib import admin
from django.urls import path,re_path
from app3.views import create_table_of_squares

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cts/<int:s>/<int:n>',create_table_of_squares),
]
