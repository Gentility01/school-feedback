from users import views
from django.urls import path

urlpatterns = [
    path("register-student", views.register_student, name="register_student"),
    path("register-lecturer", views.register_lecturer, name="register_lecturer"),
    # path("register-mainuser", views.register_mainuser, name="register_mainuser"),
    path('lecturer-login', views.lecturer_login_view, name='lecturer_login'),
    path('student-login', views.student_login_view, name='student_login'),
    # path('main-user-dashbboard', views.main_user_dashbboard, name='main_user_dashbboard'),
    path('student-dashboard', views.student_dashboard, name='student_dashboard'),
    path('student_profile', views.student_profile, name='student_profile'),

    path('lecturer-dashboard', views.lecturer_dashboard, name='lecturer_dashboard'),
    # path('lecturer-profile', views.lecturer_profile, name='lecturer_profile'),

    path('logouts', views.logout_template, name='logout_template'),
    path('logout', views.logout_view, name='logout'),


    

]