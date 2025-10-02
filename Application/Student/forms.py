# Application/Student/forms.py

from django import forms
from .models import StudentProfile, AcademicMarks, BranchChoice

# --- 1. Academic Marks Form (For High School & 10+2 Marks) ---

class AcademicMarksForm(forms.ModelForm):
    # Optional: Add validation for marks (e.g., must be between 0 and 100)
    # Custom validation can be added here if needed, but ModelForm handles basic types.
    
    class Meta:
        model = AcademicMarks
        # List all fields required for submission (Req. 4)
        fields = [
            'hsc_math', 'hsc_science', 'hsc_english', 'hsc_hindi',
            'inter_physics', 'inter_chem', 'inter_math_bio'
        ]
        # Optional: Add user-friendly labels
        labels = {
            'hsc_math': '10th Grade: Mathematics Marks (Out of 100)',
            'hsc_science': '10th Grade: Science Marks (Out of 100)',
            'inter_physics': '12th Grade: Physics Marks (Out of 100)',
            # ... and so on for the others
        }
        widgets = {
            'hsc_math': forms.NumberInput(attrs={'min': 0, 'max': 100}),
            'hsc_science': forms.NumberInput(attrs={'min': 0, 'max': 100}),
            'inter_physics': forms.NumberInput(attrs={'min': 0, 'max': 100}),
            # Apply to all fields to enforce the 0-100 rule
        }


# --- 2. Branch Choice Form (For Student Preferences) ---

# Define the choices outside the class for clarity
BRANCH_CHOICES = (
    ('CS', 'Computer Science Engineering (CSE)'),
    ('ECE', 'Electronics & Communication Engineering (ECE)'),
    ('ME', 'Mechanical Engineering (ME)'),
    ('CE', 'Civil Engineering (CE)'),
    ('EE', 'Electrical Engineering (EE)'),
    # Add more branches as per your college requirements
)

class BranchChoiceForm(forms.ModelForm):
    # Override the fields to use a cleaner Select widget
    branch_1 = forms.ChoiceField(
        choices=BRANCH_CHOICES,
        label="First Choice Branch"
    )
    branch_2 = forms.ChoiceField(
        choices=BRANCH_CHOICES,
        label="Second Choice Branch"
    )

    class Meta:
        model = BranchChoice
        fields = ['branch_1', 'branch_2']


# --- 3. (Optional) Initial Student Profile Form ---
# Assuming most of this is handled by allauth signup, but useful for extra fields
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['full_name', 'phone_number', 'date_of_birth', 'address']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }