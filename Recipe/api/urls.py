from django.urls import path
from Recipe.api.views import (
    CategoryAPIView,
    RecipeAPI,
    RecipeListCreateAPI,
    RecipeReadUpdateDeleteView,
    RecipeRetrieveUpdateDestroyAPI
)

urlpatterns = [
    path('recipe_list/', RecipeListCreateAPI.as_view(), name='recipe_list'),
    path('recipe_list/<int:pk>', RecipeRetrieveUpdateDestroyAPI.as_view(), name='recipe_detail'),

    path('category_list/', CategoryAPIView.as_view(), name='category_list'),

]