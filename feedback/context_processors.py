# feedback/context_processors.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Feedback
from .forms import ResponseForm  


def feedback_list(request):
    feedback_items = Feedback.objects.all().order_by('-created_at')
    form = ResponseForm()

    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            return redirect("/")

    return {
    
        'feedback_items': feedback_items,
        'form':form
        }


# def feedback_list(request):
#     feedback_items = Feedback.objects.all().order_by('-created_at')
#     response_form = ResponseForm()

#     if request.method == 'POST':
#         form = ResponseForm(request.POST)
#         if form.is_valid():
#             response = form.save(commit=False)
#             # Handle response logic here, similar to your existing code
#             # ...

#     context = {
#         'feedback_items': feedback_items,
#         'response_form': response_form,
#     }




