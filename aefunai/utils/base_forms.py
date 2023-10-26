from django import forms
from users.models import Student, Lecturer, MainUser
class BaseRegistrationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add Bootstrap classes and placeholders to form fields (customize as needed)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your email'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'})

    def save(self, commit=True):
        instance = super().save(commit=False)
        self.set_custom_fields(instance)
        if commit:
            instance.save()
        return instance

    def set_custom_fields(self, instance):
        raise NotImplementedError("Subclasses must implement this method")
