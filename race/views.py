from django.shortcuts import render, get_object_or_404
from race.models import Race, Track, Driver
from datetime import date

# Create your views here.
def race_list(request):
    all_races = Race.objects.all()
    context = {
        "all_races" : all_races,
    }
    return render(request, "races/races.html", context)

def upcoming_races(request):
    all_races = Track.objects.all()
    upcoming_races = [race for race in all_races if not race.has_passed]
    context = {
        "upcoming_races": upcoming_races,
    }
    return render(request, "races/upcoming_races.html", context)

def race_detail(request, name):
    race_details = get_object_or_404(Race, track__name=name)
    context = {
        "race_details": race_details
    }
    return render(request, "races/details.html", context)


def track_list(request):
    all_tracks = Track.objects.all()
    context= {
        "all_tracks" : all_tracks,
    }
    return render(request, "races/tracks.html", context)


def track_detail(request, id):
    track_details = Track.objects.get(id=id)
    context = {
        "track_details": track_details,
    }
    return render(request, "races/details.html", context)

def driver_list(request):
    all_drivers = Driver.objects.select_related('team').order_by('team__place_in_championship', 'name')
    context = {
        "all_drivers" : all_drivers,
    }
    return render(request, "drivers/drivers.html", context)
