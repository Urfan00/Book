from django.urls import path
from .views import RecipeListViev


urlpatterns = [
    path('recipe_list/', RecipeListViev.as_view(), name='recipe_list'),
]
