# Create your models here.
from django.db import models
# from django.contrib.auth.models import User
# Create your models here.

class User_Chem_e_cross(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    # alternate_phone_number = models.CharField(max_length = 100)
    college =  models.CharField(max_length=100)
    current_year = models.IntegerField()
    # permanent_address = models.TextField()
    state  = models.CharField(max_length=100)
    email = models.EmailField()
    pincode = models.IntegerField(null=True)