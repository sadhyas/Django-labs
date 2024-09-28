
from django.contrib import admin
from django.urls import path

from app2.views import greet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('greet/<str:user>/',greet),
]
