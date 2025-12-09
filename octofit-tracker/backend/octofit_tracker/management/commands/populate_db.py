from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Create users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='marvel', is_superhero=True),
            User(email='captainamerica@marvel.com', name='Captain America', team='marvel', is_superhero=True),
            User(email='batman@dc.com', name='Batman', team='dc', is_superhero=True),
            User(email='superman@dc.com', name='Superman', team='dc', is_superhero=True),
        ]
        User.objects.bulk_create(users)

        # Create activities
        user_objs = {u.email: u for u in User.objects.all()}
        Activity.objects.create(user=user_objs['ironman@marvel.com'], activity_type='run', duration=30, date=timezone.now())
        Activity.objects.create(user=user_objs['captainamerica@marvel.com'], activity_type='cycle', duration=45, date=timezone.now())
        Activity.objects.create(user=user_objs['batman@dc.com'], activity_type='swim', duration=60, date=timezone.now())
        Activity.objects.create(user=user_objs['superman@dc.com'], activity_type='fly', duration=120, date=timezone.now())

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
        Workout.objects.create(name='Situps', description='Do 30 situps', difficulty='easy')
        Workout.objects.create(name='Squats', description='Do 40 squats', difficulty='medium')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=200)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
