import re
from django import forms
from .models import STUDY_YEAR_CHOICES


def _validate_phone(value):
    """Accepts Indian formats: 10 digits, or +91/0 prefix variants."""
    cleaned = re.sub(r'[\s\-\(\)]', '', value)
    if not re.fullmatch(r'(\+91|0)?[6-9]\d{9}', cleaned):
        raise forms.ValidationError(
            "Enter a valid 10-digit Indian phone number (e.g. 9876543210 or +919876543210)."
        )


def _validate_pincode(value):
    if value and not re.fullmatch(r'[1-9]\d{5}', value):
        raise forms.ValidationError("Enter a valid 6-digit Indian pincode.")


_TEXT  = lambda ph: forms.TextInput(attrs={'class': 'input input-bordered w-full text-gray-950', 'placeholder': ph})
_AREA  = lambda ph: forms.Textarea(attrs={'class': 'textarea textarea-bordered w-full text-gray-950', 'placeholder': ph, 'rows': 3})
_EMAIL = lambda ph: forms.EmailInput(attrs={'class': 'input input-bordered w-full text-gray-950', 'placeholder': ph})
_SEL   = lambda:    forms.Select(attrs={'class': 'select select-bordered w-full text-gray-950'})


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        label='First Name',
        max_length=100,
        widget=_TEXT('First Name'),
    )
    last_name = forms.CharField(
        label='Last Name',
        max_length=100,
        widget=_TEXT('Last Name'),
    )
    email = forms.EmailField(
        label='Email Address',
        widget=_EMAIL('your@email.com'),
    )
    phone_number = forms.CharField(
        label='Phone Number',
        max_length=20,
        validators=[_validate_phone],
        widget=_TEXT('9876543210'),
    )
    alternate_phone_number = forms.CharField(
        label='Alternate Phone Number',
        max_length=20,
        required=False,
        validators=[_validate_phone],
        widget=_TEXT('Alternate Phone Number (optional)'),
    )
    college = forms.CharField(
        label='College / University',
        max_length=200,
        widget=_TEXT('College or University Name'),
    )
    current_year = forms.ChoiceField(          # was CharField — bypassed model choices entirely
        label='Current Year of Study',
        choices=[('', '— Select year —')] + STUDY_YEAR_CHOICES,
        widget=_SEL(),
    )
    permanent_address = forms.CharField(
        label='Permanent Address',
        widget=_AREA('Street, City, District'),
    )
    pincode = forms.CharField(
        label='Pincode',
        max_length=10,
        required=False,
        validators=[_validate_pincode],
        widget=_TEXT('110001'),
    )
    state = forms.CharField(
        label='State',
        max_length=100,
        widget=_TEXT('State'),
    )


class Azeo_idForm(forms.Form):
    email                  = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name             = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name              = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number           = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    alternate_phone_number = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)
    college                = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    current_year           = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    permanent_address      = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    state                  = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    pincode                = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)