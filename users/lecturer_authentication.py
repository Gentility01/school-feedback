from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .models import Lecturer
class LecturerAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, lecturer_id=None, password=None, **kwargs):
        User = get_user_model()
        try:
            lecturer = Lecturer.objects.get( lecturer_id=lecturer_id)
            return lecturer.user
        except User.DoesNotExist:
            return None
