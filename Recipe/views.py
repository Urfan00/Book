from django.shortcuts import render
from django.views.generic import ListView
from .models import Category
from .models import Recipes
from datetime import datetime





class RecipeListViev(ListView):
    model = Recipes
    template_name = 'recipes.html'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["categories"] = Category.objects.filter(is_active=True).all()

        return context
    

    def get_queryset(self):

        current_time = datetime.now().date()

        ctg = self.request.GET.get('ctg')

        if ctg:
            self.queryset = Recipes.objects.filter(category__id=ctg,category__is_active=True, show_date__lte=current_time).all()
        else:
            self.queryset = Recipes.objects.filter(category__is_active=True, show_date__lte=current_time).all()

        return super().get_queryset()
