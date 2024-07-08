from django.shortcuts import render

from Core.models import Slider


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
