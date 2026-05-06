from django.urls import path, include
from exam.admin import admin_site

urlpatterns = [
    path('admin/', admin_site.urls),
    path('', include('exam.urls')),
]
