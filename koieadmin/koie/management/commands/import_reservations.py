#### WARNING - MAKE SURE YOU SOURCE VIRTUALENV !
from django.core.management.base import BaseCommand, CommandError
from koie.models import Koie, Reservation
from django.contrib.auth.models import User

from datetime import date

f = 'earlier_reservations.txt'
lines = []
raw_data = []

with open(f, 'r') as infile:
    raw_data = infile.readlines()

def get_or_create_user(email):
    users = User.objects.filter(email=email)
    if users.count() > 1:
        pass # WHAT THE FUCK
    elif users.count() == 1:
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
        new = 0
        failed = 0
        for reservation in raw_data:
            r = Reservation()
            res = reservation.split(";") # 0: Koie, 1: epost, 2: dato
            
            reservations += 1

            # Find which koie this is
            try:
                koie = Koie.objects.get(name=res[0])
            except:
                self.stdout.write("Koie %s not found, continuing" % res[0])
                failed += 1
                continue
            r.koie_ordered = koie

            # Find or create a user
            user = get_or_create_user(res[1])
            r.ordered_by = user

            # Parse the date
            # @ TODO: +1 fails if wrong date format
            ## I hope our users use the DD/MM/YYYY format.
            input_date = res[2].split('/')
            for x in range(0, len(input_date)):
                input_date[x] = int(input_date[x])
            reservation_date = date(input_date[2], input_date[1], input_date[0])

            r.rent_start = reservation_date
            r.rent_end = reservation_date

            r.save()
            new += 1
        self.stdout.write('%s reservations looked at. %s reservations failed to parse, therefore %s new reservations were added.' % (reservations, failed, new))
