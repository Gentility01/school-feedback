from django import forms
from .models import Student, Lecturer, MainUser
from aefunai.utils.logics import generate_lecturer_id, generate_student_registration_number

# Common form fields for username, email, and full name
common_fields = {
    'username': forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your username'})),
    'email': forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})),
    'full_name': forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your fullname'})),
}

class MainUserForm(forms.ModelForm):
    class Meta:
        model = MainUser
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if MainUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        full_name = self.cleaned_data.get('full_name')
        if full_name:
            first_name, last_name = full_name.split(" ", 1)
            user.first_name = first_name
            user.last_name = last_name
            
        if commit:
            user.save()
        return user

class BaseRegistrationForm(forms.ModelForm):
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.registration_number = self.generate_registration_number()
        if commit:
            instance.save()
        return instance

class StudentRegistrationForm(BaseRegistrationForm):
    class Meta:
        model = Student
        exclude = ['registration_number', 'user']

    def generate_registration_number(self):
        return generate_student_registration_number()

class LecturerRegistrationForm(BaseRegistrationForm):
    class Meta:
        model = Lecturer
        exclude = ['lecturer_id', 'user']

    def generate_registration_number(self):
        return generate_lecturer_id()








# views  

def register_student(request):
    if request.method == 'POST':
        user_form = MainUserForm(request.POST)
        student_form = StudentRegistrationForm(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            new_user = user_form.save()
            
            if student_form.is_valid():
                student = student_form.save(commit=False)
                student.user = new_user
                student.save()
            return redirect('student_dashboard')  # Replace with the actual URL name for the student dashboard
    else:
        user_form = MainUserForm()
        student_form = StudentRegistrationForm()
    context = {
        "user_form":user_form,
        "student_form":student_form
    }
    return render(request, 'users/register_student.html', context)



def register_lecturer(request):
    if request.method == 'POST':
        main_form = MainUserForm(request.POST)
        lectuere_form = LecturerRegistrationForm(request.POST)
        if main_form.is_valid() and lectuere_form.is_valid():
            new_user = main_form.save()
            if lectuere_form.is_valid():
                lectuere = lectuere_form.save(commit=False)
                lectuere.user = new_user
                lectuere.save()
            
            return redirect('lecturer_dashboard')  # Replace with the actual URL name for the lecturer dashboard
    else:
        main_form = MainUserForm()
        lectuere_form = LecturerRegistrationForm()
    
    context = {
        "main_form":main_form,
        "lectuere_form":lectuere_form
    }
    return render(request, 'users/register_lecturer.html',context)


# login  

def student_login_view(request):
    if request.method == 'POST':
        registration_number = request.POST['registration_number']

        user = StudentAuthenticationBackend().authenticate(request, registration_number=registration_number)
        if user is not None:
            # User is authenticated, set the backend attribute and log them in
            user.backend = 'django.contrib.auth.backends.ModelBackend'  # Specify the authentication backend
            login(request, user)
            return redirect('student_dashboard')  # Redirect to student dashboard or desired URL
        else:
            # Authentication failed, add an error message
            messages.error(request, 'Invalid registration number.')

    return render(request, 'users/student_login.html')



def lecturer_login_view(request):
    if request.method == 'POST':
        lecturer_id = request.POST['id_number']
        try:
            user = LecturerAuthenticationBackend().authenticate(request, lecturer_id=lecturer_id)
            
            if user is not None:
                # User is authenticated, log them in
                user.backend = 'django.contrib.auth.backends.ModelBackend'  # Specify the authentication backend
                login(request, user)
                return redirect('lecturer_dashboard')  # Redirect to lecturer dashboard or desired URL
            else:
                messages.error(request, 'Invalid Identity number.')
        except ObjectDoesNotExist:
            messages.error(request, 'Invalid Identity number.')

    return render(request, 'users/lecturer_login.html')
