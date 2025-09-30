from django.shortcuts import render
from django.shortcuts import render

def student_login(request):
    return render(request, 'index.html', {}) 

def student_signup(request):
    return render(request, 'signup.html', {}) 

def student_login(request):
  
    return render(request, 'index.html', {}) 

def student_signup(request):
    return render(request, 'index.html', {}) 


def data_submission(request):
    return render(request, 'placeholder_form.html', {}) 

def student_dashboard(request):
    return render(request, 'placeholder_dashboard.html', {}) 

