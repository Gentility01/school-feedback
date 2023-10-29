from django.db import models
from django.contrib.auth.models import AbstractUser
from aefunai.utils.choices import Faculty, Gender, Administrator, Departments
# Create your models here.

class MainUser(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=200)



    def __str__(self):
        return f"{self.username} - {self.email}"


class Student(models.Model):
    user = models.OneToOneField(MainUser, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20,choices=Gender.choices,  default=Gender.Male,)
    faculty = models.CharField(max_length=50, choices=Faculty.choices, default=Faculty.agric)
    registration_number = models.CharField(max_length=10, unique=True, blank=True, null=True)
    # Add other student-related fields here


   
            
    def __str__(self):
        return self.user.username

class Lecturer(models.Model):
    user = models.OneToOneField(MainUser, on_delete=models.CASCADE)
    department = models.CharField(max_length=50, choices=Departments.choices, default=Departments.ART)
    lecturer_id = models.CharField(max_length=10, unique=True, blank=True, null=True)
    position = models.CharField(max_length=50, choices=Administrator.choices, default=Administrator.dean)
    # Add other lecturer-related fields here

    def __str__(self):
        return self.user.username