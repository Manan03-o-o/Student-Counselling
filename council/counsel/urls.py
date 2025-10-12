from django.urls import path
from . import views

urlpatterns = [
    path("", views.student_dashboard, name="student_dashboard"),
    path("profile/", views.edit_profile, name="edit_profile"),
    path("marks/", views.submit_marks, name="submit_marks"),
    path("apply/", views.apply_branch, name="apply_branch"),
    path("payment/", views.upload_payment, name="upload_payment"),
    path("admin-panel/", views.admin_dashboard, name="admin_dashboard"),
    path("admin-panel/allocate/<int:student_id>/", views.allocate_branch, name="allocate_branch"),
    path("admin-panel/verify-payment/<int:student_id>/", views.verify_payment, name="verify_payment"),

]
