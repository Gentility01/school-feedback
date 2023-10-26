from django import forms
from .models import Student, Lecturer, MainUser
from aefunai.utils.logics import generate_lecturer_id, generate_student_registration_number
from aefunai.utils.choices import Gender, Faculty, Departments, Administrator
# Common form fields for username, email, and full name
common_fields = {
    # 'username': forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your username'})),
    # 'email': forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})),
    # 'full_name': forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your fullname'})),
    # 'password':forms.CharField(widget=forms.PasswordInput())
}

class MainUserForm(forms.ModelForm):
    class Meta:
        model = MainUser
        fields = ['full_name', 'username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.update(common_fields)  # Update fields with common_fields
        

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
        if commit:
            instance.save()
        return instance

class StudentRegistrationForm(BaseRegistrationForm):
    gender = forms.ChoiceField(choices=Gender.choices, initial= Gender.Male, widget=forms.Select(attrs={'class': 'form-control'}))
    faculty = forms.ChoiceField(choices=Faculty.choices,  widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Student
        exclude = ['registration_number', 'user']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.registration_number = self.generate_registration_number()
        if commit:
            instance.save()
        return instance

    def generate_registration_number(self):
        return generate_student_registration_number()

class LecturerRegistrationForm(BaseRegistrationForm):
    position = forms.ChoiceField(choices=Administrator.choices, widget=forms.Select(attrs={'class': 'form-control'}))
    department = forms.ChoiceField(choices=Departments.choices,  widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Lecturer
        exclude = ['lecturer_id', 'user']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.lecturer_id = self.generate_lecturer_id()
        if commit:
            instance.save()
        return instance

    def generate_lecturer_id(self):
        return generate_lecturer_id()













