from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from Account.models import Account
from .forms import ChangePasswordForm, CustomSetPasswordForm, LoginForm, RegistrationFormModel, ResetPasswordForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .tokens import account_activation_token
from django.utils.encoding import force_str, force_bytes
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from BookShop.settings import EMAIL_HOST_USER
from django.contrib import messages


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm


def login_view(request):

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')

            user = authenticate(request, username = username, password = password)

            if user:
                login(request, user)
                return redirect("/")
            else:
                return redirect('login')

    context = {
        'form': form
    }

    return render(request, 'accounts/login.html', context)


class CustomRegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = RegistrationFormModel
    success_url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            subject = 'Activate your account'
            current_site = get_current_site(request)
            message = render_to_string('accounts/confirmation_email.html', {
                'user' : user,
                'domain': current_site.domain,
                'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
                'token' : account_activation_token.make_token(user)
            })
            from_email = EMAIL_HOST_USER
            to_email = request.POST['email']
            send_mail(subject, message, from_email, [to_email, ])

            return redirect('login')
        return render(request, self.template_name, {'form':form})


def activate(requset, uidb64, token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = Account.objects.filter(pk=uid, is_active=False).first()

    if user is not None and account_activation_token.check_token(user, token):
        messages.success(requset, 'Your profile is activated')
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        messages.error(requset, 'Your session is expired')
        return redirect('/')


def register_view(request):

    form = RegistrationFormModel()

    if request.method == 'POST':

        form = RegistrationFormModel(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = False
            user.save()
        else:
            return redirect('register')
        return redirect('login')

    context = {
        'form' : form
    }

    return render(request, 'accounts/register.html', context)


class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name='accounts/change_password.html'
    form_class= ChangePasswordForm
    success_url = reverse_lazy('login')


class ResetPasswordView(PasswordResetView):
    template_name = 'accounts/forget_password.html'
    form_class = ResetPasswordForm
    email_template_name = 'accounts/reset_password_email.html'
    subject_template_name = 'accounts/reset_password_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      "If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."

    success_url = reverse_lazy('login')


class ResetPasswordConfirmView(PasswordResetConfirmView):
    template_name='accounts/reset_password_confirm.html'
    form_class=CustomSetPasswordForm
    success_url = reverse_lazy('reset_password_complete')