# Application/Student/urls.py

from django.urls import path
from . import views 
# This imports the functions (like student_login) from Application/Student/views.py

urlpatterns = [
    # 1. Authentication Paths
    # We keep these for consistency, but allauth handles the real logic
    path('login/', views.student_login, name='student_login'), 
    path('signup/', views.student_signup, name='student_signup'),
    
    # 2. Post-Login Core Paths
    path('dashboard/', views.student_dashboard, name='student_dashboard'), 
    
    # 3. Data Submission Forms (Req. 4)
    path('data-submission/', views.data_submission, name='data_submission'), 
    
    # Note: You can also use the commented-out path for a root/home page if needed later
    # path('', views.home, name='home'), 
]
path('admin-login/', views.admin_login, name='admin_login'),