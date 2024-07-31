from django import forms
from Account.models import Account
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder' : 'Enter your username'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder' : 'Password'
            }
        )
    )


class RegistrationFormModel(UserCreationForm):

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : "Your password"
            }
        ),
        label='Password'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : "Confirm password"
            }
        ),
        label='Confirm Password'
    )

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'first_name' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' :"Enter your first name",
                }
            ),
            'last_name' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' :"Enter your last name"
                }
            ),
            'username' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' :"Username"
                }
            ),
            'email' : forms.EmailInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' :"E-mail"
                }
            )
        }
