from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import StudentRegistrationForm, LecturerRegistrationForm, MainUserForm
from.models import Student, Lecturer
from users.lecturer_authentication import LecturerAuthenticationBackend
from users.student_authentication import StudentAuthenticationBackend
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from aefunai.utils.view_logics import register_user, login_view
from feedback.models import Feedback
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import user_passes_test

# Create your views here.
@user_passes_test(lambda user: user.is_superuser)
def register_student(request):
    return register_user(request, 'student')

@user_passes_test(lambda user: user.is_superuser)
def register_lecturer(request):
    return register_user(request, 'lecturer')


# Student login view
def student_login_view(request):
    return login_view(
        request,
        authentication_backend=StudentAuthenticationBackend,
        redirect_url='student_dashboard',
        request_field='registration_number',
        error_message='Invalid registration number.',
        template_name='users/student_login.html'  # Specify the student login template
    )


# Lecturer login view
def lecturer_login_view(request):
    return login_view(
        request,
        authentication_backend=LecturerAuthenticationBackend,
        redirect_url='lecturer_dashboard',
        request_field='lecturer_id',
        error_message='Invalid Identity number.',
        template_name='users/lecturer_login.html'  # Specify the lecturer login template
    )


@login_required(login_url='student_login')
def student_dashboard(request):
    student = Student.objects.get(user=request.user)
    student_feedback = Feedback.objects.filter(student=student)
    context = {
        
        "student_feedback":student_feedback
    }
    return render(request, "users/student_dasboard.html", context)


def lecturer_dashboard(request):
    lecturer = Lecturer.objects.get(user = request.user)
    context = {
        "lecturer":lecturer
    }
    return render(request, "users/lectuere_dashboard.html", context)


@login_required(login_url='student_login')
def student_profile(request):
    pages = "s_profile"

    context = {
        "pages":pages
    }
    return render(request, "users/studentprofile.html", context)

def logout_template(request):
    return render(request, "users/logout_template.html")


def logout_view(request):
    logout(request)
    return redirect('logout_template')

