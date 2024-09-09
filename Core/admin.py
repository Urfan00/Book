from django.contrib import admin
from Core.models import Contact, Slider, Subscriber
from import_export.admin import ImportExportModelAdmin
from modeltranslation.admin import TranslationAdmin


class SliderAdmin(ImportExportModelAdmin, TranslationAdmin):
    fieldsets = (
        ('EN', {'fields': ('title_en', 'description_en')}),  # English fields
        ('AZ', {'fields': ('title_az', 'description_az')}),  # Azerbaijani fields
        ('RU', {'fields': ('title_ru', 'description_ru')}),  # Russian fields
        ('Additional', {'fields': ('image', )}),  # Non-translated fields
    )
    list_display = ['id', 'title', 'image', 'description']
    list_display_links = ['id', 'title']
    search_fields = ['title']


class ContactAdmin(ImportExportModelAdmin):
    list_display = ['id', 'fullname', 'email', 'subject', 'created_at', 'updated_at']
    list_display_links = ['id', 'fullname']
    search_fields = ['fullname', 'email', 'subject']
    list_filter = ['created_at', 'updated_at']


class SubscriberAdmin(ImportExportModelAdmin):
    list_display = ('id', 'email', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('id', 'email')
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('email', )




admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Slider, SliderAdmin)

