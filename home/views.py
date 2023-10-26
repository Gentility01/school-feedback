from django.shortcuts import render, redirect
from feedback.models import Feedback, Response, Vote
from feedback.forms import ResponseForm
from users.models import Student

def homePage(request):
    feedback_items = Feedback.objects.all().order_by('-created_at')
    form = ResponseForm()
    user = request.user
    student = None
    feedback = None
    voted_feedback_ids = None
    
    # Initialize feedback_responses variable as an empty queryset
    feedback_responses = Response.objects.none()
    
    if request.method == "POST":
        feedback_id = request.POST.get('vote')
        print("Feedback ID:", feedback_id)
        feedback = Feedback.objects.get(pk=feedback_id)
        try:
            student = request.user.student
        except Student.DoesNotExist:
            student = None

        # creating response
        form = ResponseForm(request.POST)
        if form.is_valid():
            administrator = request.user.lecturer
            response = form.save(commit=False)
            response.feedback = feedback
            response.administrator = administrator
            response.save()

        # voting
        has_voted = False
        if student:
            has_voted = Vote.objects.filter(student=student, feedback=feedback).exists()

        if not has_voted and student:
            vote = Vote(student=student, feedback=feedback)
            vote.save()

    # Check if the user has already voted for this feedback
    voted_feedback_ids = Vote.objects.filter(student=student).values_list('feedback__id', flat=True) if student else []
    
    # Get all responses for the selected feedback
    if feedback:
        feedback_responses = Response.objects.filter(feedback=feedback)
    
    print("Feedback Responses:", feedback_responses)
    context = {
        'feedback_items': feedback_items,
        'form': form,
        'feedback_responses': feedback_responses,
    }

    return render(request, "home/index.html", context)
