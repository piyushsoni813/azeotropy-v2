from django import forms
from .models import Extendeduser

class RegisterForm(forms.Form):
    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(attrs={
            'class': 'input input-bordered w-full text-gray-950',
            'placeholder': 'First Name'
        })
    )
    last_name = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(attrs={
            'class': 'input input-bordered w-full text-gray-950',
            'placeholder': 'Last Name'
        })
    )
    email = forms.EmailField(
        label='Email Address',
        widget=forms.EmailInput(attrs={
            'class': 'input input-bordered w-full text-gray-950',
            'placeholder': 'Gmail Preferred'
        })
    )
    phone_number = forms.CharField(
        label='Phone Number',
        widget=forms.TextInput(attrs={
            'class': 'input input-bordered w-full text-gray-950',
            'placeholder': 'Phone Number'
        })
    )
    alternate_phone_number = forms.CharField(
        label='Alternate Phone Number',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'input input-bordered w-full text-gray-950',
            'placeholder': 'Alternate Phone Number'
        })
    )
    college = forms.CharField(
        label='Your College/University Name',
        widget=forms.TextInput(attrs={
            'class': 'input input-bordered w-full text-gray-950',
            'placeholder': 'College/University Name'
        })
    )
    current_year = forms.CharField(
        label='Current Year of Study',
        widget=forms.TextInput(attrs={
            'class': 'input input-bordered w-full text-gray-950',
            'placeholder': 'Current Year'
        })
    )
    permanent_address = forms.CharField(
        label='Permanent Address',
        widget=forms.Textarea(attrs={
            'class': 'textarea textarea-bordered w-full text-gray-950',
            'placeholder': 'Permanent Address'
        })
    )
    pincode = forms.CharField(
        label='Pincode',
        widget=forms.TextInput(attrs={
            'class': 'input input-bordered w-full text-gray-950',
            'placeholder': 'Pincode'
        })
    )
    state = forms.CharField(
        label='State',
        widget=forms.TextInput(attrs={
            'class': 'input input-bordered w-full text-gray-950',
            'placeholder': 'State'
        })
    )



class Azeo_idForm(forms.Form):
    # username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), )
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), )
    alternate_phone_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False )
    college = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    current_year = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}),)
    permanent_address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':3}))
    state = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    pincode = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=True )





   