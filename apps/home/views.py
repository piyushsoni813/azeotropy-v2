from django.shortcuts import render

def header(request):
    return render(request, 'main/header.html')  # Use relative path

def home(request):
    return render(request, 'main/home.html')  # Use relative path

def footer(request):
    return render(request, 'main/footer.html')  # Use relative path

def competitions(request):
    return render(request, 'competition/competitions.html')  # Use relative path

def events(request):
    return render(request, 'events/event.html')  # Use relative path

def workshop(request):
    return render(request, 'workshop/workshops.html')  # Use relative path

def team(request):
    return render(request, 'team/team.html')  # Use relative path

def sponsor(request):
    return render(request, 'sponsors/sponsor.html')  # Use relative path

def schedule(request):
    return render(request, 'main/schedule.html')  # Use relative path
