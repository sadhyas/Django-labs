
from django.contrib import admin
from django.urls import path,re_path
from app7.views import reg 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/', reg), 
]
