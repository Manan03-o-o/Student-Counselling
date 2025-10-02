from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from allauth.account.views import signup # Optional: to redirect if needed
# from .models import StudentProfile, AcademicMarks, Allocation # Import these later when writing business logic
# Application/Student/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction # Good practice for saving multiple related models
from .models import StudentProfile, AcademicMarks, BranchChoice # <-- UNCOMMENT THIS LINE (or similar)
from .forms import StudentProfileForm, AcademicMarksForm, BranchChoiceForm # <-- NEW IMPORT

# ... (student_login, student_signup, admin_login, student_dashboard views here) ...

@login_required
def data_submission(request):
    
    # Try to get existing data or initialize blank forms
    try:
        profile = request.user.studentprofile
        marks_instance = AcademicMarks.objects.get(profile=profile)
        choices_instance = BranchChoice.objects.get(profile=profile)
    except (StudentProfile.DoesNotExist, AcademicMarks.DoesNotExist, BranchChoice.DoesNotExist):
        # If any object doesn't exist, create a new instance placeholder
        profile = request.user.studentprofile
        marks_instance = None
        choices_instance = None
    
    
    if request.method == 'POST':
        # 1. Bind forms to POST data (and existing instances if present)
        marks_form = AcademicMarksForm(request.POST, instance=marks_instance)
        choices_form = BranchChoiceForm(request.POST, instance=choices_instance)
        
        if marks_form.is_valid() and choices_form.is_valid():
            
            with transaction.atomic():
                # 2. Save Academic Marks
                marks = marks_form.save(commit=False)
                marks.profile = profile
                marks.total_10_plus_2_marks = marks.inter_physics + marks.inter_chem + marks.inter_math_bio # Calculate total
                marks.save()

                # 3. Save Branch Choices
                choices = choices_form.save(commit=False)
                choices.profile = profile
                choices.save()
                
                # Update the student profile status
                profile.data_submitted = True 
                profile.save()
            
            return redirect('student_dashboard') # Redirect after successful save
        
    else:
        # 4. Display the forms (GET request)
        marks_form = AcademicMarksForm(instance=marks_instance)
        choices_form = BranchChoiceForm(instance=choices_instance)
    
    context = {
        'marks_form': marks_form,
        'choices_form': choices_form,
        'page_title': 'Academic & Preference Submission'
    }
    
    return render(request, 'data_submission.html', context)

# --- PUBLIC PAGES ---

def student_login(request):
    """
    Renders the custom login page template. 
    Actual login submission is handled by django-allauth at /accounts/login/.
    """
    # Renders the custom index.html from the root /Templates folder
    return render(request, 'index.html', {})


def student_signup(request):
    """
    Renders the custom signup page template. 
    Actual registration submission is handled by django-allauth at /accounts/signup/.
    """
    # Renders the signup.html from the root /Templates folder
    return render(request, 'signup.html', {})


def admin_login(request):
    """
    Renders the dedicated Admin Login link page (Req. 6).
    Admins will use the Django Admin site for core functions.
    """
    return render(request, 'admin_login.html', {})


# --- PROTECTED PAGES (Requires User to be Logged In) ---

@login_required 
def student_dashboard(request):
    """
    Displays the student's status, data submission link, and allocation status.
    (This is the main view after successful login).
    """
    # --- PLACEHOLDER CONTEXT (Replace with actual database lookups later) ---
    # Fetching data for the currently logged-in user (request.user)
    context = {
        'data_submitted': False,      # Fetched from StudentProfile.data_submitted
        'allocated_branch': None,     # Fetched from Allocation.allocated_branch
        'allocation_accepted': False, # Fetched from Allocation.is_accepted
        'payment_verified': False,    # Fetched from Allocation.is_payment_verified
        'total_marks': 'N/A',         
        'student_rank': 'N/A',        
    }
    # --- END PLACEHOLDER CONTEXT ---

    return render(request, 'dashboard.html', context) 


@login_required
def data_submission(request):
    """
    Handles the student's personal information, marks, and branch choices form (Req. 4).
    """
    # In a real app, you would handle GET (display form) and POST (save data) here.
    
    # Placeholder response
    if request.method == 'POST':
        # Add logic here to save data to AcademicMarks and BranchChoice models
        # Then redirect to the dashboard
        return redirect('student_dashboard')
        
    return render(request, 'data_submission.html', {}) # Renders the form template
