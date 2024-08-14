from rest_framework import serializers
from Core.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'fullname', 'email', 'subject', 'message', 'created_at', 'updated_at']

