from django.shortcuts import redirect, render
from Core.forms import ContactFormModel
from Core.models import Contact, Slider
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy


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

        forms = ContactFormModel(data=request.POST)

        if forms.is_valid():
            forms.save()
            messages.success(request, 'form submit oldu')

            return redirect('contact')

    context = {
        'forms' : forms
    }

    return render(request, 'contact.html', context)


class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactFormModel
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'form submit oldu')
        return super().form_valid(form)
