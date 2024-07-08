from django.urls import path
from .views import about, index, recipe, user_profile

urlpatterns = [
    path('', index, name='index'),
    path('recipe_list/', recipe, name='recipe_list'),
    path('about/', about, name='about'),
    path('user_profile/', user_profile, name='user_profile'),
]
