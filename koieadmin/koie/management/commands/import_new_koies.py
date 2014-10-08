#### WARNING - MAKE SURE YOU SOURCE VIRTUALENV !
from django.core.management.base import BaseCommand, CommandError
from koie.models import Koie

import json

# Import
f = 'koiedump.json'
json_data = ""

with open(f, 'r') as infile:
    raw_data = infile.read()
  #  print(raw_data)
    json_data = json.loads(raw_data)
 #   print(json_data)

#print(json_data["1"])
class Command(BaseCommand):
    args = "test1"
    help = "test2"

    def handle(self, *args, **options):
        koies = 0
        new = 0
        existing = 0
        for koie in json_data:
            koies += 1
            k = Koie()
            koie = json_data[koie]
            
            # Check if koie already exists

#            print(koie['name'])
#            print(Koie.objects.filter(name=koie['name']), Koie.objects.filter(name=koie['name']).count())
            if Koie.objects.filter(name=koie['name']).count() > 0:
                existing += 1
                continue

            k.name = koie['name']
            k.address = koie['address']
            k.location = koie['location']
            k.zip_code = koie['zip_code']
            k.num_beds = koie['num_beds']
            k.save()
            new += 1
        self.stdout.write('%s koies looked at. %s were already in the system, so %s new koies were added.' % (koies, existing, new))

"""
x = 0
for koie in json_data:
    k = Koie()
    k.name = koie['name']
    k.address = koie['address']
    k.location = koie['location']
    k.zip_code = koie['zip_code']
    k.num_beds = koie['num_beds']
    k.save()
    x += 1
print('Added %s koies to koiesys' % x)
"""
