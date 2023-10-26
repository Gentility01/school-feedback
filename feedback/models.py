from django.db import models

# Create your models here.

from users.models import Student, Lecturer

class Feedback(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.student.user.username}"

class Vote(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    upvote = models.BooleanField(default=False)
    # created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['student', 'feedback']  # Ensure each user can vote

    def __str__(self):
        return f"Vote by {self.student.user.username} on Feedback {self.feedback.id}"

class Response(models.Model):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    administrator = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    response_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response by {self.administrator.user.username} to Feedback {self.feedback.id}"
