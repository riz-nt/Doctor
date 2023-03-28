from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

# Create your views here.
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = doctor_details.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

class RegisterDoctorView(APIView):
    permission_classes = [AllowAny,]
    serializer_class = RegisterDoctorSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']
            doctor_id = serializer.validated_data['doctor_id']
            category = serializer.validated_data['category']
            password = serializer.validated_data['password']
            users = doctor_details.objects.create(
                username=username,
                email=email,
                doctor_id=doctor_id,
                category=category,
                password=password,
            )
            users.save()
        return Response('Doctor created successfully')