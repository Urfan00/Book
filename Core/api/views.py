import django_filters.rest_framework
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from Core.api.serializers import ContactSerializer
from Core.models import Contact
from rest_framework.pagination import LimitOffsetPagination

from Recipe.api.pagination import SmallPageNumberPagination

class ContactListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    pagination_class = SmallPageNumberPagination


class ContactRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
