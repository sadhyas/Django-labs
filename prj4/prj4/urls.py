
from django.contrib import admin
from django.urls import path, re_path
from app4.views import vc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vc/<str:sentence>', vc),
]
