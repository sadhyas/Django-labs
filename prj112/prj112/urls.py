from django.contrib import admin
from django.urls import path
from app112.views import construct_pdf_from_model 

admin.site.site_header="My Site Header" 
admin.site.site_title="My Site Title" 
admin.site.index_title="My Site Index"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('construct_pdf_from_model/', construct_pdf_from_model),
]