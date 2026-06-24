from django import forms

class RegistrationForm(forms.Form):
    YEAR_CHOICES = [
        ("BTech", "BTech"),
        ("MTech", "MTech"),
        ("PhD", "PhD"),
    ]

    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    year_of_study = forms.ChoiceField(choices=YEAR_CHOICES)  # Dropdown field
    college_name = forms.CharField(max_length=200)
