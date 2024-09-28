from django.contrib import admin
from django.urls import path
from app9.views import add_project

admin.site.site_header="My Site Header"
admin.site.site_title="My Site Title"
admin.site.index_title="My Site Index"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_project/', add_project),
]
