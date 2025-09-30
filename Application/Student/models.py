from django.db import models
from django.contrib.auth.models import User 
# Note: For production-ready apps, use a CustomUser model, but User is fine for starting.

# --- 1. Student Profile Model ---
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True) 
    
    # Personal Information
    full_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15, unique=True, help_text="Used for OTP/Verification later")
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField()

    # Field to check if the student has completed the data submission form
    data_submitted = models.BooleanField(default=False) 
    
    # Admin status for later (Req. 6)
    is_admin = models.BooleanField(default=False) 

    def __str__(self):
        return self.full_name


# --- 2. Academic Marks Model (Req. 4) ---
class AcademicMarks(models.Model):
    profile = models.OneToOneField(StudentProfile, on_delete=models.CASCADE)

    # High School (HSC/10th Grade) Marks
    hsc_math = models.IntegerField(verbose_name="Maths Marks (10th)")
    hsc_science = models.IntegerField(verbose_name="Science Marks (10th)")
    hsc_english = models.IntegerField(verbose_name="English Marks (10th)")
    hsc_hindi = models.IntegerField(verbose_name="Hindi/Local Lang. Marks (10th)")

    # 10+2 (Intermediate) Marks
    inter_physics = models.IntegerField(verbose_name="Physics Marks (10+2)")
    inter_chem = models.IntegerField(verbose_name="Chemistry Marks (10+2)")
    inter_math_bio = models.IntegerField(verbose_name="Maths/Biology Marks (10+2)")

    @property
    def total_10_plus_2_marks(self):
        # Calculate total marks for ranking (Req. 7)
        return self.inter_physics + self.inter_chem + self.inter_math_bio

    def __str__(self):
        return f"Marks for {self.profile.full_name}"


# --- 3. Branch Choice Model (Req. 7) ---
class BranchChoice(models.Model):
    profile = models.OneToOneField(StudentProfile, on_delete=models.CASCADE)
    
    # Example branches (define choices later)
    branch_1 = models.CharField(max_length=100, verbose_name="First Choice Branch")
    branch_2 = models.CharField(max_length=100, verbose_name="Second Choice Branch")

    def __str__(self):
        return f"Choices for {self.profile.full_name}"


# --- 4. Allocation and Payment Model (Req. 7) ---
class Allocation(models.Model):
    profile = models.OneToOneField(StudentProfile, on_delete=models.CASCADE)
    
    # Allocation Status
    allocated_branch = models.CharField(max_length=100, null=True, blank=True)
    is_accepted = models.BooleanField(default=False) # Student chooses to accept

    # Payment/Verification Status
    payment_receipt = models.FileField(upload_to='receipts/', null=True, blank=True) # Submission of receipt
    is_payment_verified = models.BooleanField(default=False) # Admin verification

    # Final Offer Letter
    offer_letter_generated = models.BooleanField(default=False)

    def __str__(self):
        return f"Allocation for {self.profile.full_name}"