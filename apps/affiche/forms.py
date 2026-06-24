from django import forms
from .models import AfficheTeam

class AfficheTeamForm(forms.ModelForm):
    member2_id = forms.CharField(max_length=10, required=False, help_text="Enter AzeoID of member 2")

    class Meta:
        model = AfficheTeam
        fields = ['team_name', 'abstract']

    def clean_member2_id(self):
        member2_id = self.cleaned_data.get('member2_id')
        if member2_id:
            try:
                member2 = AzeoProfile.objects.get(azeo_id=member2_id)
                return member2_id
            except AzeoProfile.DoesNotExist:
                raise forms.ValidationError("Invalid AzeoID for member 2")
        return member2_id