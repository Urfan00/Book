from django.shortcuts import redirect, render
from .models import Category, Story, Tag
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView


def story(request):

    q_category = request.GET.get('category')

    print('==>', request.GET)

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


class StoryList(ListView):
    model = Story
    template_name = 'story.html'
    context_object_name = 'stories'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["categories"] = Category.objects.exclude(is_active=False).all()

        return context

    def get_queryset(self):

        category = self.request.GET.get('category')

        if category:
            self.queryset = Story.objects.filter(category__id=category, category__is_active=True, show_date__lte=datetime.date(datetime.now())).all()
        else:
            self.queryset = Story.objects.filter(category__is_active=True, show_date__lte=datetime.date(datetime.now())).all()

        return super().get_queryset()
    


@login_required
def story_detail(request, id):

    story = Story.objects.filter(id=id, category__is_active = True).first()

    if not story:
        return redirect('story_list')


    tags = Tag.objects.all()

    categories = Category.objects.filter(is_active=True).all()

    context = {
        'story' : story,
        'tags' : tags,
        'categories' : categories
    }

    return render(request, 'single.html', context)
