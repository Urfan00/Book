from django.urls import path
from Recipe.api.views import RecipeAPI, RecipeReadUpdateDeleteView

urlpatterns = [
    path('recipe_list/', RecipeAPI.as_view(), name='recipe_list'),
    path('recipe_list/<int:pk>', RecipeReadUpdateDeleteView.as_view(), name='recipe_detail'),
]
