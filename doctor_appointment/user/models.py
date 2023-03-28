from django.db import models

# Create your models here.
class user_details(models.Model):
    username = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    date = models.DateField(auto_now=True, null=True)
    time = models.TimeField(auto_now=True, null=True)
    status = models.CharField(max_length=250, default=True)