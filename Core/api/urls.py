from django.urls import path

from Core.api.views import ContactListCreateAPIView, ContactRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('contact_list/', ContactListCreateAPIView.as_view(), name='contact_list'),
    path('contact_list/<int:pk>', ContactRetrieveUpdateDestroyAPIView.as_view(), name='contact_list'),
]
