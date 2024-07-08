from django.contrib import admin
from .models import Category, Story, Tag


admin.site.register([Tag, Category, Story])
