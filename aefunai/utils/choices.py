from django.db import models
from django.utils import timezone


class Gender(models.TextChoices):
    Male = ("male", "Male")
    Female = ("female", "Female")



class Faculty(models.TextChoices):
    agric = ("Faculty of Agriculture", "Faculty of Agriculture")
    bms = ("Faculty of Basic Medical Sciences", "Faculty of Basic Medical Sciences")
    biology = ("Faculty of Biological Science", "Faculty of Biological Science")
    medical_science = ("Faculty of College of Medical Sciences", "Faculty of College of Medical Sciences")
    education = ("Faculty of Education", "Faculty of Education")
    engineering = ("Faculty of Engineering and Technology", "Faculty of Engineering and Technology")
    environmental_science = ("Faculty of Environmental Sciences", "Faculty of Environmental Sciences")
    humanities = ("Faculty of Humanities", "Faculty of Humanities")
    management_science = ("Faculty of Management Sciences", "Faculty of Management Sciences")
    physical_science = ("Faculty of Physical Science", "Faculty of Physical Science")
    social_science = ("Faculty of Social Sciences", "Faculty of Social Sciences")


class Administrator(models.TextChoices):
    provost = ("Provost/Chief Academic Officer", "Provost/Chief Academic Officer")
    dean = ("Dean of Students", "Dean of Students")
    registrar = ("Registrar", "Registrar")
    director_of_admission = ("Director of Admissions", "Director of Admissions")
    financial_director = ("Financial Aid Director", "Financial Aid Director")
    chief_financial_officer = ("Chief Financial Officer", "Chief Financial Officer")
    director_human_resources = ("Director of Human Resources", "Director of Human Resources")
    campus_facilities_director = ("Director of Campus Facilities/Physical Plant", "Director of Campus Facilities/Physical Plant")
    chief_information_officer = ("Chief Information Officer", "Chief Information Officer")
    research_programs_director = ("Director of Research and Sponsored Programs", "Director of Research and Sponsored Programs")
    alumni_relations_director = ("Alumni Relations Director", "Alumni Relations Director")
    international_programs_director = ("International Programs Director", "International Programs Director")
    diversity_inclusion_officer = ("Diversity and Inclusion Officer", "Diversity and Inclusion Officer")
    athletic_director = ("Athletic Director", "Athletic Director")



class Departments(models.TextChoices):
    ENGLISH = 'English', 'English Department'
    MATH = 'Math', 'Mathematics Department'
    SCIENCE = 'Science', 'Science Department'
    SOCIAL_STUDIES = 'Social Studies', 'Social Studies Department'
    FOREIGN_LANGUAGE = 'Foreign Language', 'Foreign Language Department'
    PHYSICAL_EDUCATION = 'Physical Education', 'Physical Education Department'
    ART = 'Art', 'Art Department'
    MUSIC = 'Music', 'Music Department'
    TECHNOLOGY = 'Technology', 'Technology Department'
    SPECIAL_EDUCATION = 'Special Education', 'Special Education Department'
    COUNSELING = 'Counseling', 'Counseling Department'
    ADMINISTRATION = 'Administration', 'Administration Department'





    
