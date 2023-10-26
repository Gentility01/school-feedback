from django.contrib import admin
from .models import MainUser, Student, Lecturer
# Register your models here.

admin.site.register(MainUser)
admin.site.register(Student)
admin.site.register(Lecturer)
