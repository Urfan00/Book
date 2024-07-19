from django.shortcuts import redirect, render
from Core.forms import ContactFormModel
from Core.models import Contact, Slider
from django.contrib import messages


def index(request):

    sliders = Slider.objects.all()

    context = {
        'sliders' : sliders
    }

    return render(request, 'index.html', context)

def recipe(request):
    return render(request, 'recipes.html')

def about(request):
    return render(request, 'about.html')

def user_profile(request):
    return render(request, 'user-profile.html')


def contact(request):

    forms = ContactFormModel()

    if request.method == 'POST':

        request.GET
        request.POST
        forms = ContactFormModel(data=request.POST)

        if forms.is_valid():
            forms.save()
            messages.success(request, 'form submit oldu')

            return redirect('contact')

    context = {
        'forms' : forms
    }

    return render(request, 'contact.html', context)