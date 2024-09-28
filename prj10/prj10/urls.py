from django.contrib import admin
from django.urls import path
from app10.views import StudentListView,StudentDetailView

admin.site.site_header="My Site Header" 
admin.site.site_title="My Site Title" 
admin.site.index_title="My Site Index"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('st_list/',StudentListView.as_view()),
    path('st_detail/<int:pk>/',StudentDetailView.as_view()),
]
 