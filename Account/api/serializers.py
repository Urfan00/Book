from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from Account.models import Account



class UserDetailSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class CustomTokenObtainPairView(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        serializer = UserDetailSerialzier(user)
        data.update(serializer.data)
        return data
