# institution_app/registration_utils.py
import string
import random
from users.models import Student, Lecturer
import datetime

def generate_student_registration_number():
    # Generate a unique registration number (e.g., 'AEF20230001')
    prefix = 'AEF/'
    current_year = datetime.datetime.now().year  # Get the current year
    year = str(current_year)
    last_student = Student.objects.all().order_by('-id').first()
    
    if last_student:
        last_id = int(last_student.registration_number[-4:])
        new_id = last_id + 1
    else:
        new_id = 1
    
    new_id_str = str(new_id).zfill(4)
    return f'{prefix}{year}{new_id_str}'

def generate_lecturer_id():
    # Generate a unique lecturer ID (e.g., 'LEC/20230001')
    prefix = 'LEC/'
    current_year = datetime.datetime.now().year  # Get the current year
    year = str(current_year)
    last_lecturer = Lecturer.objects.all().order_by('-id').first()
    
    if last_lecturer:
        last_id = int(last_lecturer.lecturer_id[-4:])
        new_id = last_id + 1
    else:
        new_id = 1
    
    new_id_str = str(new_id).zfill(4)
    return f'{prefix}{year}{new_id_str}'




def generate_lecturer_id():
    # Generate a unique lecturer ID (e.g., 'LEC/20230001')
    prefix = 'LEC/'
    year = str(2023)  # You can change this to get the current year dynamically
    last_lecturer = Lecturer.objects.all().order_by('-id').first()
    if last_lecturer:
        last_id = int(last_lecturer.lecturer_id[-4:])
        new_id = last_id + 1
    else:
        new_id = 1
    new_id_str = str(new_id).zfill(4)
    return f'{prefix}{year}{new_id_str}'
