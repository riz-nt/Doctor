from django.urls import path, include
from .views import *

urlpatterns = [
    path('doctor_details/', RegisterDoctorView.as_view()),
    path('doctor_details_view/', DoctorViewSet.as_view({'get':'list'})),
]
