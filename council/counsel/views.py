from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import StudentProfile, Marks, Application, PaymentReceipt
from .forms import ProfileForm, MarksForm, ApplicationForm, PaymentForm
from .models import BRANCH_CHOICES

@login_required
def student_dashboard(request):
    # If the user is the hardcoded admin, redirect to admin dashboard
    if request.user.username == "admin":
        return redirect("admin_dashboard")

    # Normal student dashboard
    profile, _ = StudentProfile.objects.get_or_create(user=request.user)
    marks = getattr(profile, "marks", None)
    app = getattr(profile, "application", None)
    pay = getattr(profile, "paymentreceipt", None)
    return render(request, "counsel/student_dashboard.html",
                  {"profile": profile, "marks": marks, "app": app, "pay": pay})

@login_required
def edit_profile(request):
    profile, _ = StudentProfile.objects.get_or_create(user=request.user)
    form = ProfileForm(request.POST or None, instance=profile)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("student_dashboard")
    return render(request, "counsel/form.html", {"form": form, "title": "Edit Profile"})

@login_required
def submit_marks(request):
    profile, _ = StudentProfile.objects.get_or_create(user=request.user)
    marks = getattr(profile, "marks", None)
    form = MarksForm(request.POST or None, instance=marks)
    if request.method == "POST" and form.is_valid():
        obj = form.save(commit=False)
        obj.student = profile
        obj.save()
        return redirect("student_dashboard")
    return render(request, "counsel/form.html", {"form": form, "title": "Submit Marks"})

@login_required
def apply_branch(request):
    profile, _ = StudentProfile.objects.get_or_create(user=request.user)
    app = getattr(profile, "application", None)
    form = ApplicationForm(request.POST or None, instance=app)
    if request.method == "POST" and form.is_valid():
        obj = form.save(commit=False)
        obj.student = profile
        obj.save()
        return redirect("student_dashboard")
    return render(request, "counsel/form.html", {"form": form, "title": "Apply Branch"})

@login_required
def upload_payment(request):
    profile, _ = StudentProfile.objects.get_or_create(user=request.user)
    pay = getattr(profile, "paymentreceipt", None)
    form = PaymentForm(request.POST or None, request.FILES or None, instance=pay)
    if request.method == "POST" and form.is_valid():
        obj = form.save(commit=False)
        obj.student = profile
        obj.save()
        return redirect("student_dashboard")
    return render(request, "counsel/form.html", {"form": form, "title": "Upload Payment"})

# ---------------- ADMIN ----------------
def is_admin(user):
    return user.is_staff

@user_passes_test(is_admin)
def admin_dashboard(request):
    students = StudentProfile.objects.exclude(user__username="admin")
    ranked = sorted(students, key=lambda s: s.marks.total_12 if hasattr(s, "marks") else 0, reverse=True)
    return render(request, "counsel/admin_dashboard.html", {"students": ranked})

  # make sure this is imported at top

@user_passes_test(lambda u: u.username=="admin")  # optional: restrict to hardcoded admin
def allocate_branch(request, student_id):
    student = get_object_or_404(StudentProfile, id=student_id)

    if request.method == "POST":
        branch = request.POST.get("branch")
        student.allocated_branch = branch
        student.save()
        return redirect("admin_dashboard")

    # Pass the branch choices to the template
    return render(request, "counsel/allocate.html", {
        "student": student,
        "branch_choices": BRANCH_CHOICES
    })

@user_passes_test(lambda u: u.username=="admin")
def verify_payment(request, student_id):
    student = get_object_or_404(StudentProfile, id=student_id)
    if hasattr(student, "paymentreceipt"):
        student.paymentreceipt.verified = True
        student.paymentreceipt.save()
        student.payment_verified = True
        student.save()
    return redirect("admin_dashboard")


# ---------------- ADMIN ----------------
def is_admin(user):
    return user.is_authenticated and user.username == "admin"
