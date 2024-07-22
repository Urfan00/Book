from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationFormModel


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


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
