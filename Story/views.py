from django.shortcuts import render
from .models import Category, Story
from datetime import datetime


def story(request):

    q_category = request.GET.get('category')

    categories = Category.objects.exclude(is_active=False).all()

    if q_category:
        stories = Story.objects.filter(category__id=q_category, category__is_active=True, show_date__lte=datetime.date(datetime.now())).all()
    else:
        stories = Story.objects.filter(category__is_active=True, show_date__lte=datetime.date(datetime.now())).all()


    context = {
        'stories': stories,
        'categories': categories,
    }

    return render(request, 'story.html', context)