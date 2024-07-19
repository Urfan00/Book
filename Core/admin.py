from django.contrib import admin
from Core.models import Contact, Slider


class SliderAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'description']
    list_display_links = ['id', 'title']
    search_fields = ['title']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullname', 'email', 'subject', 'created_at', 'updated_at']
    list_display_links = ['id', 'fullname']
    search_fields = ['fullname', 'email', 'subject']
    list_filter = ['created_at', 'updated_at']



admin.site.register(Contact, ContactAdmin)
admin.site.register(Slider, SliderAdmin)

