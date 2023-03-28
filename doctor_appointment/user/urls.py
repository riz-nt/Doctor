from django.urls import path, include
# from rest_framework import routers
# from doctor_appointment.user import views
from .views import *

urlpatterns = [
    path('user_details/', RegisterUserView.as_view()),
    path('user_details_view/', UserViewSet.as_view({'get':'list'})),
    path('user_login/', LoginUserView.as_view()),
]
