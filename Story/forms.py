from django import forms
from .models import StoryComment



class StoryCommentFormModel(forms.ModelForm):
    class Meta:
        model = StoryComment
        fields = ['message']

        labels = {
            'message' : 'Message'
        }

        widgets = {
            'message' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'rows' : 7,
                    'placeholder' :"Write your message"
                }
            ),
        }