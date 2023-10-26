from django.urls import path
from feedback import views



urlpatterns = [
    path("submit-feedback", views.submit_feedback, name = "submit_feedback" ),
]