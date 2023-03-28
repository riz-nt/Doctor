from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.Serializer):
    class Meta:
        model = user_details
        fields = ['username', 'email', 'password']

class RegisterUserSerializer(serializers.Serializer):
    username = serializers.CharField(error_messages={'message':'Username Required'})
    email = serializers.CharField(error_messages={'message':'Email Required'})
    password = serializers.CharField(error_messages={'message':'Password Required'})

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        try:
            user_login = user_details.objects.get(username=username, password=password)
        except:
            user_login = None
        if not user_login:
            raise serializers.ValidationError({'message':'Username does not exist'})
        return data