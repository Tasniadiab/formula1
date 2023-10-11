from django.test import TestCase
from race.models import Race, Track, Driver, Team
from datetime import date

class RaceTestCase(TestCase):
    def setUp(self):
        """
        Setup teams, drivers and one track
        """
        team_rbr = Team.objects.create(name="Oracle Red Bull Racing")
        self.rbr_driver1 = Driver.objects.create(
            name="Max Verstappen", country="Netherlands", team=team_rbr
        )
        self.rbr_driver2 = Driver.objects.create(
            name="Sergio Perez", country="Mexico", team=team_rbr
        )

        team_am = Team.objects.create(name="Aston Martin")
        self.am_driver1 = Driver.objects.create(
            name="Fernando Alonso", country="Spain", team=team_am
        )
        self.am_driver2 = Driver.objects.create(
            name="Lance Stroll", country="Canada", team=team_am
        )

        # Setup track
        self.monza_track = Track.objects.create(
            name="Autodromo Nazionale di Monza",
            location="Italy",
            url="https://en.wikipedia.org/wiki/Monza_Circuit",
        )

    def test_race_grid(self):
        """
        Create a 'Race' and check the grid position
        """
        race_date = date(2022, 9, 11)
        Race.objects.create(
            driver=self.rbr_driver1, 
            track=self.monza_track, 
            grid=1, 
            date=race_date
        )
        Race.objects.create(
            driver=self.rbr_driver2, 
            track=self.monza_track, 
            grid=6, 
            date=race_date
        )
        Race.objects.create(
            driver=self.am_driver1, 
            track=self.monza_track, 
            grid=18, 
            date=race_date
        )
        Race.objects.create(
            driver=self.am_driver2, 
            track=self.monza_track, 
            grid=19, 
            date=race_date
        )

        monza_race = Race.objects.filter(track=self.monza_track, date=race_date)
        
        # 1st place was super max (the first element of the queryset)
        self.assertEqual(monza_race.first().driver.name, "Max Verstappen")
        # "Last" place was stroll (the last element of the queryset)
        self.assertEqual(monza_race.last().driver.name, "Lance Stroll")
        

        print(monza_race)
        print(monza_race.first())
        # Output sample:
        # <QuerySet [
        #     <Race: Max Verstappen grid 1>, 
        #     <Race: Sergio Perez grid 6>, 
        #     <Race: Fernando Alonso grid 18>, 
        #     <Race: Lance Stroll grid 19>
        # ]>