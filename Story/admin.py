from django.contrib import admin
from .models import Category, Story, StoryComment, Tag


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'is_active', 'created_at', 'updated_at']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    list_filter = [ 'is_active', 'created_at', 'updated_at']


class StoryCommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'story','created_at', 'updated_at']
    list_display_links = ['id', 'user']
    search_fields = ['user']
    list_filter = ['created_at', 'updated_at']


admin.site.register(StoryComment, StoryCommentAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.register([Tag, Story])
