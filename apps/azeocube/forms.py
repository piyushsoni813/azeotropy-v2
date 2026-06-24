from django import forms
from .models import AzeoCubeTeam
from apps.azeoid.models import AzeoProfile

class AzeoIDRegistrationForm(forms.Form):
    azeo_id = forms.CharField(max_length=10, help_text="Enter your AzeoID")
    
    def clean_azeo_id(self):
        azeo_id = self.cleaned_data.get('azeo_id')
        try:
            profile = AzeoProfile.objects.get(azeo_id=azeo_id)
            return azeo_id
        except AzeoProfile.DoesNotExist:
            raise forms.ValidationError("Invalid AzeoID. Please create an AzeoID first.")

class AzeoCubeTeamForm(forms.ModelForm):
    member2_id = forms.CharField(max_length=10, required=False, help_text="Enter AzeoID of member 2")
    member3_id = forms.CharField(max_length=10, required=False, help_text="Enter AzeoID of member 3")
    member4_id = forms.CharField(max_length=10, required=False, help_text="Enter AzeoID of member 4")

    class Meta:
        model = AzeoCubeTeam
        fields = ['team_name']

    def clean_member2_id(self):
        member2_id = self.cleaned_data.get('member2_id')
        if member2_id:
            try:
                member2 = AzeoProfile.objects.get(azeo_id=member2_id)
                return member2_id
            except AzeoProfile.DoesNotExist:
                raise forms.ValidationError("Invalid AzeoID for member 2")
        return member2_id

    def clean_member3_id(self):
        member3_id = self.cleaned_data.get('member3_id')
        if member3_id:
            try:
                member3 = AzeoProfile.objects.get(azeo_id=member3_id)
                return member3_id
            except AzeoProfile.DoesNotExist:
                raise forms.ValidationError("Invalid AzeoID for member 3")
        return member3_id

    def clean_member4_id(self):
        member4_id = self.cleaned_data.get('member4_id')
        if member4_id:
            try:
                member4 = AzeoProfile.objects.get(azeo_id=member4_id)
                return member4_id
            except AzeoProfile.DoesNotExist:
                raise forms.ValidationError("Invalid AzeoID for member 4")
        return member4_id