from django.db import models

# Defined at module level so forms can import without referencing the class
STUDY_YEAR_CHOICES = [
    ('B.Tech 1st Year', '1st Year B.Tech'),
    ('B.Tech 2nd Year', '2nd Year B.Tech'),
    ('B.Tech 3rd Year', '3rd Year B.Tech'),
    ('B.Tech 4th Year', '4th Year B.Tech'),
    ('M.Tech 1st Year', '1st Year M.Tech'),
    ('M.Tech 2nd Year', '2nd Year M.Tech'),
    ('Ph.D 1st Year',   '1st Year Ph.D'),
    ('Ph.D 2nd Year',   '2nd Year Ph.D'),
    ('Ph.D 3rd Year',   '3rd Year Ph.D'),
    ('Ph.D 4th Year',   '4th Year Ph.D'),
]


class Extendeduser(models.Model):
    first_name             = models.CharField(max_length=100)
    last_name              = models.CharField(max_length=100)
    phone_number           = models.CharField(max_length=20)          # was IntegerField — can't store +91 or leading zeros
    alternate_phone_number = models.CharField(max_length=20, blank=True)
    college                = models.CharField(max_length=200)
    current_year           = models.CharField(max_length=50, choices=STUDY_YEAR_CHOICES, default='B.Tech 1st Year')
    permanent_address      = models.TextField()
    state                  = models.CharField(max_length=100)
    email                  = models.EmailField(unique=True)           # unique=True added — no duplicate CAs
    pincode                = models.CharField(max_length=10, blank=True)  # was IntegerField — leading zeros matter

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"


class Azeo_id_user(models.Model):
    first_name             = models.CharField(max_length=100)
    last_name              = models.CharField(max_length=100)
    phone_number           = models.IntegerField()
    alternate_phone_number = models.CharField(max_length=100)
    college                = models.CharField(max_length=100)
    current_year           = models.CharField(max_length=50, choices=STUDY_YEAR_CHOICES, default='B.Tech 1st Year')
    permanent_address      = models.TextField()
    state                  = models.CharField(max_length=100)
    email                  = models.EmailField()
    pincode                = models.IntegerField(null=True)
    azeo_id                = models.CharField(max_length=100, default=1)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.azeo_id})"