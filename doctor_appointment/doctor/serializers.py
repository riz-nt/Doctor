from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class DoctorSerializer(serializers.Serializer):
    class Meta:
        model = doctor_details
        fields = ['username', 'email', 'doctor_id', 'category', 'password']

class RegisterDoctorSerializer(serializers.Serializer):
    username = serializers.CharField(error_messages={'message':'Username Required'})
    email = serializers.CharField(error_messages={'message':'Email Required'})
    doctor_id = serializers.CharField(error_messages={'message':'Doctor ID Required'})
    category = serializers.CharField(error_messages={'message':'Category Required'})
    password = serializers.CharField(error_messages={'message':'Password Required'})