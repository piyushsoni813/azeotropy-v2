from django.db import models

# Create your models here.
class COPuser(models.Model):
    member1 = models.CharField(max_length=100)