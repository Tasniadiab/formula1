from django.urls import path
from race.views import track_list, track_detail, driver_list, upcoming_races

urlpatterns = [
    path("races/", track_list, name="track_list"),
    path("upcoming/", upcoming_races, name="upcoming_races"),
    path("races/<int:id>/", track_detail, name="track_detail"),
    path("drivers/", driver_list, name= "driver_list")
]
