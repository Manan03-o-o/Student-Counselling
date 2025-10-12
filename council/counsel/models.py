from django.db import models
from django.contrib.auth.models import User

BRANCH_CHOICES = [
    ("CSE", "Computer Science"),
    ("ECE", "Electronics"),
    ("ME", "Mechanical"),
]

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    allocated_branch = models.CharField(max_length=10, choices=BRANCH_CHOICES, blank=True)
    payment_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Marks(models.Model):
    student = models.OneToOneField(StudentProfile, on_delete=models.CASCADE)
    math_hs = models.IntegerField(default=0)
    science_hs = models.IntegerField(default=0)
    english_hs = models.IntegerField(default=0)
    hindi_hs = models.IntegerField(default=0)
    physics = models.IntegerField(default=0)
    chemistry = models.IntegerField(default=0)
    maths = models.IntegerField(default=0)

    @property
    def total_12(self):
        return self.physics + self.chemistry + self.maths

class Application(models.Model):
    student = models.OneToOneField(StudentProfile, on_delete=models.CASCADE)
    first_choice = models.CharField(max_length=10, choices=BRANCH_CHOICES)
    second_choice = models.CharField(max_length=10, choices=BRANCH_CHOICES)

class PaymentReceipt(models.Model):
    student = models.OneToOneField(StudentProfile, on_delete=models.CASCADE)
    receipt = models.FileField(upload_to="receipts/")
    verified = models.BooleanField(default=False)
