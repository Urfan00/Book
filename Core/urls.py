from django.urls import path
from .views import ContactView, about, contact, index, user_profile

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('user_profile/', user_profile, name='user_profile'),
]
