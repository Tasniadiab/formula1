from django.contrib import admin
from race.models import Track, Team, Driver, Race

# Register your models here.

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "country",
        "team_principle",
        "place_in_championship",
    )


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location",
        "url",
        "date",
        "has_passed",
    )


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = (
      "name",
      "country",
      "team",
    )


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = (
        "track",
        "driver",
        "grid",
        "date",
        "has_passed",
        "result",
        "id",
        # "comments",
    )