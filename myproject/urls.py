from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('firstdjango.urls')),# I called mine "firstdjango"
    path('admin/', admin.site.urls),
]