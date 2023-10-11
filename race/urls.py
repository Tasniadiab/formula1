from django.urls import path
from race.views import track_list, track_detail

urlpatterns = [
    path("races/", track_list, name="track_list"),
    path("<int:id>/", track_detail, name="track_detail"),
]
