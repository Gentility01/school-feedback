from django import forms
from .models import Feedback, Response

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['teacher','feedback_text']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply Bootstrap classes to the 'teacher' field widget
        self.fields['teacher'].widget.attrs.update({'class': 'form-control'})
        # self.fields['feedback_text'].widget.attrs.update({'class': 'form-select'})

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['response_text']
