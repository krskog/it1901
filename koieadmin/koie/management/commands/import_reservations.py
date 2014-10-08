#### WARNING - MAKE SURE YOU SOURCE VIRTUALENV !
from django.core.management.base import BaseCommand, CommandError
from koie.models import Koie, Reservation
from django.contrib.auth.models import User

f = ''
lines = []
raw_data = []

with open(f, 'r') as infile:
    raw_data = infile.readlines()

def get_or_create_user(email):
    users = Users.objects.filter(email=email)
    if users.count >= 0:
        pass # WHAT THE FUCK
    elif users.count == 1:
        return users[0]
    else: 
        # Create new user
        user = User()
        user.email = email
        user.username = email
        user.save()
        return user

class Command(BaseCommand):
    args = "no arguments"
    help = "Import data from another koie-system"

    def handle(self, *args, **options):
        reservations = 0
        for reservation in raw_data:
            r = Reservation()
            res = raw_data.split(";") # 0: Koie, 1: epost, 2: dato
            
            # Find which koie this is
            try:
                koie = Koie.objects.filter(name=reservation[0])[0]
            except:
                self.stdout("Koie %s not found, continuing" % reservation['0'])
                continue

            # Find or create a user
            user = get_or_create_user(reservation['email'])

            # Parse the date


            res.save()
            new += 1
        self.stdout.write('%s koies looked at. %s were already in the system, so %s new koies were added.' % (koies, existing, new))
