from django.db import models
# from django.contrib.auth.models import User
# Create your models here.

class Extendeduser(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    alternate_phone_number = models.CharField(max_length = 100)
    college =  models.CharField(max_length=100)
    STUDY_YEAR_CHOICES = [
        # B.Tech years
        ('B.Tech 1st Year', '1st Year B.Tech'),
        ('B.Tech 2nd Year', '2nd Year B.Tech'),
        ('B.Tech 3rd Year', '3rd Year B.Tech'),
        ('B.Tech 4th Year', '4th Year B.Tech'),
        # M.Tech years
        ('M.Tech 1st Year', '1st Year M.Tech'),
        ('M.Tech 2nd Year', '2nd Year M.Tech'),
        # Ph.D. years
        ('Ph.D 1st Year', '1st Year Ph.D'),
        ('Ph.D 2nd Year', '2nd Year Ph.D'),
        ('Ph.D 3rd Year', '3rd Year Ph.D'),
        ('Ph.D 4th Year', '4th Year Ph.D'),
    ]

    current_year = models.CharField(
        max_length=50,
        choices=STUDY_YEAR_CHOICES,
        default='B.Tech 1st Year',
    )
    permanent_address = models.TextField()
    state  = models.CharField(max_length=100)
    email = models.EmailField()
    pincode = models.IntegerField(null=True)
    # user = models.OneToOneField(User, on_delete= models.CASCADE)

class Azeo_id_user(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    alternate_phone_number = models.CharField(max_length = 100)
    college =  models.CharField(max_length=100)
    STUDY_YEAR_CHOICES = [
        # B.Tech years
        ('B.Tech 1st Year', '1st Year B.Tech'),
        ('B.Tech 2nd Year', '2nd Year B.Tech'),
        ('B.Tech 3rd Year', '3rd Year B.Tech'),
        ('B.Tech 4th Year', '4th Year B.Tech'),
        # M.Tech years
        ('M.Tech 1st Year', '1st Year M.Tech'),
        ('M.Tech 2nd Year', '2nd Year M.Tech'),
        # Ph.D. years
        ('Ph.D 1st Year', '1st Year Ph.D'),
        ('Ph.D 2nd Year', '2nd Year Ph.D'),
        ('Ph.D 3rd Year', '3rd Year Ph.D'),
        ('Ph.D 4th Year', '4th Year Ph.D'),
    ]

    current_year = models.CharField(
        max_length=50,
        choices=STUDY_YEAR_CHOICES,
        default='B.Tech 1st Year',
    )
    permanent_address = models.TextField()
    state  = models.CharField(max_length=100)
    email = models.EmailField()
    pincode = models.IntegerField(null=True)
    azeo_id = models.CharField(max_length=100,default=1)
    # user = models.OneToOneField(User, on_delete= models.CASCADE)

