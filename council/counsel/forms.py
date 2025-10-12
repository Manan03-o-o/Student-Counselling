from django import forms
from .models import StudentProfile, Marks, Application, PaymentReceipt

class ProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ["phone", "address"]

class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        exclude = ["student"]

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["first_choice", "second_choice"]

class PaymentForm(forms.ModelForm):
    class Meta:
        model = PaymentReceipt
        fields = ["receipt"]
