from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = user_details.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class RegisterUserView(APIView):
    permission_classes = [AllowAny,]
    serializer_class = RegisterUserSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            users = user_details.objects.create(
                username=username,
                email=email,
                password=password,
            )
            users.save()
        return Response('User created successfully')

class LoginUserView(APIView):
    permission_classes = [AllowAny,]
    serializer_class = LoginUserSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user_login = user_details.objects.get(username=username, password=password)
            contents = {
                'username': username,
                'password': password,
            }
            response_content = {
                'data' : contents,
            }
        return Response(response_content)
