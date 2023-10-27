from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .models import Lecturer
class LecturerAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, lecturer_id=None, password=None, **kwargs):
        User = get_user_model()
        try:
            # Check if a lecturer with the specified lecturer_id exists
            lecturer = Lecturer.objects.get(lecturer_id=lecturer_id)
            # If a lecturer exists, return the associated user
            return lecturer.user
        except Lecturer.DoesNotExist:
            # If the lecturer does not exist, return None to indicate authentication failure
            return None
