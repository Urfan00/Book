from django.urls import path
from .views import ContactView, about, contact, export_view, index, user_profile

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('user_profile/', user_profile, name='user_profile'),
    path('export_view/', export_view, name='export_view'),
]
