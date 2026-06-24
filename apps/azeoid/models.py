from django.db import models

class Registration(models.Model):
    YEAR_CHOICES = [
        ("BTech", "BTech"),
        ("MTech", "MTech"),
        ("PhD", "PhD"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    year_of_study = models.CharField(max_length=10, choices=YEAR_CHOICES)  # Dropdown choices
    college_name = models.CharField(max_length=200)
    azeoid = models.CharField(max_length=255, unique=True)  # Generated Azeoid

    def __str__(self):
        return f"{self.name} ({self.azeoid})"
