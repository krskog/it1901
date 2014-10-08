#### WARNING - MAKE SURE YOU SOURCE VIRTUALENV !
import json

koies = {
    '1': {
        'name': 'Koie Name 1',
        'address': 'Koie 1 Address',
        'zip_code': 'Koie 1 zip code',
        'location': 'Koie 1 location',
        'num_beds': 3,
    },
}
f = 'koiedump.json'
with open(f, 'w') as out:
    json.dump(koies, out, sort_keys=True, indent=4, ensure_ascii=False)

