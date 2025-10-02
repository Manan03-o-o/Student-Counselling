# config/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Allauth URLs (handles /accounts/login, /accounts/signup, etc.)
    path('accounts/', include('allauth.urls')), 
    
    # Your main application URLs (default root access)
    path('', include('Application.Student.urls')), 
]