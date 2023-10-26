from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .models import Student

class StudentAuthenticationBackend(ModelBackend):
    def authenticate(self, request, registration_number=None, password=None, **kwargs):
        User = get_user_model()
        try:
            student = Student.objects.get(registration_number=registration_number)
            return student.user
            # user = student.user
            # if user.check_password(password):
            #     return user
        except Student.DoesNotExist:
            return None
