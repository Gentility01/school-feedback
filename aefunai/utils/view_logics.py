from django.shortcuts import render, redirect
from django.contrib.auth import login
from users.forms import StudentRegistrationForm, LecturerRegistrationForm, MainUserForm
# from users.lecturer_authentication import LecturerAuthenticationBackend
# from users.student_authentication import StudentAuthenticationBackend
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

def register_user(request, user_type):
    if request.method == 'POST':
        user_form = MainUserForm(request.POST)
        
        if user_type == 'student':
            specific_form = StudentRegistrationForm(request.POST)
        elif user_type == 'lecturer':
            specific_form = LecturerRegistrationForm(request.POST)
        else:
            specific_form = None
        
        if user_form.is_valid() and specific_form and specific_form.is_valid():
            new_user = user_form.save()
            
            if specific_form.is_valid():
                specific_user = specific_form.save(commit=False)
                specific_user.user = new_user
                specific_user.save()
            
            if user_type == 'student':
                messages.success(request, 'The registration was successful you can register more Student!')
                return redirect('register_student')  # Replace with the actual URL name for the student dashboard
            elif user_type == 'lecturer':
                messages.success(request, 'The registration was successful you can register more Lecturer!')
                return redirect('register_lecturer')  # Replace with the actual URL name for the lecturer dashboard
                
    else:
        user_form = MainUserForm()
        
        if user_type == 'student':
            specific_form = StudentRegistrationForm()
        elif user_type == 'lecturer':
            specific_form = LecturerRegistrationForm()
        else:
            specific_form = None

    context = {
        "user_form": user_form,
        "specific_form": specific_form,
        "user_type": user_type
    }

    template_name = f'users/register_{user_type}.html'
    return render(request, template_name, context)




def login_view(request, authentication_backend, redirect_url, request_field, error_message, template_name):
    if request.method == 'POST':
        user_id = request.POST[request_field]
        try:
            user = authentication_backend().authenticate(request, **{request_field: user_id})
            
            if user is not None:
                # User is authenticated, log them in
                user.backend = 'django.contrib.auth.backends.ModelBackend'  # Specify the authentication backend
                login(request, user)
                return redirect(redirect_url)  # Redirect to the desired URL
            else:
                messages.error(request, error_message)
        except ObjectDoesNotExist:
            messages.error(request, error_message)

    return render(request, template_name)