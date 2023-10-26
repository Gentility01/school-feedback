from django.urls import path
from home import views

urlpatterns = [
    path("", views.homePage, name="homePage"),
    # path('respond_to_feedback/<int:feedback_id>/', views.respond_to_feedback, name='respond_to_feedback'),

]