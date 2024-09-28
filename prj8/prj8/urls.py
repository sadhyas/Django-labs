from django.contrib import admin 
from django.urls import path, re_path 
from app8.views import reg 
admin.site.site_header="My Site Header" 
admin.site.site_title="My Site Title" 
admin.site.index_title="My Site Index" 
urlpatterns = [ 
    path('secretadmin/', admin.site.urls),
    path('reg/', reg),
]
