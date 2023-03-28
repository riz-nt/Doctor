from django.db import models

# Create your models here.
class category(models.Model):
    category_name = models.CharField(max_length=250)
    date = models.DateField(auto_now=True, null=True)
    time = models.TimeField(auto_now=True, null=True)
    status = models.CharField(max_length=250, default=True)