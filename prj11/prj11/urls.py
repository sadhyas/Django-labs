
from django.contrib import admin
from django.urls import path
from app11.views import construct_csv_from_model 

admin.site.site_header="My Site Header" 
admin.site.site_title="My Site Title" 
admin.site.index_title="My Site Index"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('construct_csv_from_model/', construct_csv_from_model),
]
