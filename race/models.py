from django.db import models
from datetime import date
# Create your models here.


class Track(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    url = models.URLField()
    date = models.DateField(null=True)

    def __str__(self):
        return self.name
    @property
    def has_passed(self):
        return self.date < date.today()


class Team(models.Model):
    name = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    team_principle = models.CharField(max_length=250)
    place_in_championship = models.SmallIntegerField(null = True, blank = True)

    def __str__(self):
        return self.name


class Driver(models.Model):
    name = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    team = models.ForeignKey(
        Team,
        related_name = "drivers_team",
        on_delete = models.CASCADE
    )
    races = models.ManyToManyField(
        Track, 
        through="Race"
        )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
    

class Race(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    grid = models.IntegerField()
    date = models.DateField()
    # comments = models.ManyToManyField(Comment, blank=True)

    @property
    def has_passed(self):
        return self.date < date.today()

    class Meta:
        ordering = ["date"]

    def result(self):
        return f"{self.driver.name} grid {self.grid}"

    def __str__(self):
        return self.track.name

