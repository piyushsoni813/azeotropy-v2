from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AzeoCubeTeam
from .forms import AzeoIDRegistrationForm, AzeoCubeTeamForm
from apps.azeoid.models import AzeoProfile

def verify_azeoid(request):
    if request.method == 'POST':
        form = AzeoIDRegistrationForm(request.POST)
        if form.is_valid():
            azeo_id = form.cleaned_data['azeo_id']
            profile = AzeoProfile.objects.get(azeo_id=azeo_id)
            request.session['verified_azeo_id'] = azeo_id
            return redirect('azeocube:register_team')
    else:
        form = AzeoIDRegistrationForm()
    return render(request, 'azeocube/verify_azeoid.html', {'form': form})

def register_team(request):
    if 'verified_azeo_id' not in request.session:
        messages.error(request, 'Please verify your AzeoID first')
        return redirect('azeocube:verify_azeoid')

    leader_profile = AzeoProfile.objects.get(azeo_id=request.session['verified_azeo_id'])

    if request.method == 'POST':
        form = AzeoCubeTeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.team_leader = leader_profile

            # Add team members if provided
            if form.cleaned_data['member2_id']:
                team.member2 = AzeoProfile.objects.get(azeo_id=form.cleaned_data['member2_id'])
            if form.cleaned_data['member3_id']:
                team.member3 = AzeoProfile.objects.get(azeo_id=form.cleaned_data['member3_id'])
            if form.cleaned_data['member4_id']:
                team.member4 = AzeoProfile.objects.get(azeo_id=form.cleaned_data['member4_id'])

            team.save()
            del request.session['verified_azeo_id']
            messages.success(request, 'Team registered successfully!')
            return redirect('azeocube:registration_success')
    else:
        form = AzeoCubeTeamForm()

    return render(request, 'azeocube/register_team.html', {'form': form})