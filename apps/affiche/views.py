from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AfficheTeam
from .forms import AfficheTeamForm
from apps.azeoid.models import AzeoProfile
from apps.azeocube.forms import AzeoIDRegistrationForm

def verify_azeoid(request):
    if request.method == 'POST':
        form = AzeoIDRegistrationForm(request.POST)
        if form.is_valid():
            azeo_id = form.cleaned_data['azeo_id']
            profile = AzeoProfile.objects.get(azeo_id=azeo_id)
            request.session['verified_azeo_id'] = azeo_id
            return redirect('affiche:register_team')
    else:
        form = AzeoIDRegistrationForm()
    return render(request, 'affiche/verify_azeoid.html', {'form': form})

def register_team(request):
    if 'verified_azeo_id' not in request.session:
        messages.error(request, 'Please verify your AzeoID first')
        return redirect('affiche:verify_azeoid')

    leader_profile = AzeoProfile.objects.get(azeo_id=request.session['verified_azeo_id'])

    if request.method == 'POST':
        form = AfficheTeamForm(request.POST, request.FILES)
        if form.is_valid():
            team = form.save(commit=False)
            team.team_leader = leader_profile

            if form.cleaned_data['member2_id']:
                team.member2 = AzeoProfile.objects.get(azeo_id=form.cleaned_data['member2_id'])

            team.save()
            del request.session['verified_azeo_id']
            messages.success(request, 'Team registered successfully!')
            return redirect('affiche:registration_success')
    else:
        form = AfficheTeamForm()

    return render(request, 'affiche/register_team.html', {'form': form})