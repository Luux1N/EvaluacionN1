from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # admin
    path('', include('agenda.urls')), # urls de la app
]