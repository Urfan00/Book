from django import forms
from .models import Contact



class ContactFormModel(forms.ModelForm):
    class Meta:
        model = Contact
        # fields ='__all__'
        fields = ['fullname', 'email', 'subject', 'message']
        # exclude = ['message']


        labels = {
            'fullname' : 'Full Name',
            'email' : 'E-mail',
        #     'subject' : 'Subject',
        #     'message' : 'Message'
        }

        widgets = {
            'fullname' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' :"Enter your full name",
                }
            ),
        #     'last_name' : forms.TextInput(
        #         attrs={
        #             'class' : 'form-control',
        #             'placeholder' :"Enter your last name"
        #         }
        #     ),
            'email' : forms.EmailInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' :"E-mail"
                }
            ),
            'subject' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' :"Enter your subject"
                }
            ),
            'message' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'rows' : 7,
                    'placeholder' :"Write your message"
                }
            ),
        }