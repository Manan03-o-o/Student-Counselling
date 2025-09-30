from django.urls import path
from . import views 
# Import the views module from the current directory (Student app)

urlpatterns = [
    # path('', views.home, name='home'),  # Example: landing page
    path('login/', views.student_login, name='student_login'), 
    path('signup/', views.student_signup, name='student_signup'),
    
    # Placeholder for the data submission form (Phase 3)
    path('data-submission/', views.data_submission, name='data_submission'), 
    
    # Placeholder for the dashboard (Phase 3)
    path('dashboard/', views.student_dashboard, name='student_dashboard'), 
]
# Application/Student/urls.py
from django.urls import path
from . import views 

urlpatterns = [
    # Existing Login Path
    path('login/', views.student_login, name='student_login'), 

    # New Sign Up Path
    path('signup/', views.student_signup, name='student_signup'),

    # ... other paths ...
]