from django.contrib import admin
from .models import Recipes



class RecipesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'show_date', 'user', 'category', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'category__name']
    list_filter = ['created_at', 'updated_at']

admin.site.register(Recipes, RecipesAdmin)
