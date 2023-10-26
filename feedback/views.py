from django.shortcuts import render, redirect, get_object_or_404
from .models import Feedback, Response
from .forms import FeedbackForm, ResponseForm
# Create your views here.

# def feedback_list(request):
#     feedback_items = Feedback.objects.all()
#     return render(request, 'feedback/feedback_list.html', {'feedback_items': feedback_items})


def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.student = request.user.student  # Assuming you have a way to get the current student
            feedback.save()
            return redirect('homePage')
    else:
        form = FeedbackForm()
    context = {'form':form}
    return render(request, 'feedback/create_feedback.html', context)


# def respond_to_feedback(request, feedback_id):
#     feedback = get_object_or_404(Feedback, pk=feedback_id)

#     if request.method == 'POST':
#         form = ResponseForm(request.POST)
#         if form.is_valid():
#             response = form.save(commit=False)
#             response.feedback = feedback
#             response.administrator = request.user.lecturer  # Assuming you have a way to get the current lecturer
#             response.save()
#             return redirect('feedback_list')
#     else:
#         form = ResponseForm()
#     return render(request, 'feedback/respond_to_feedback.html', {'form': form, 'feedback': feedback})
