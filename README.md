# IT1901 - Prosjekt 1
## Gruppe 21
---

Hei! Her lagrer vi kildekoden vår.

Takk GitHub!<3

## Installation

### Utviklermiljø for python-pakker

Utviklermiljø gjør det mulig å bruke de samme pakkene i forskjellige versjoner på samme system. Dette gjør det da mulig å ha flere Django-installasjoner som følger forskjellige versjoner.

Det anbefales bruk av *virtual environments* i Python. Fra og med Python 3.4 følger dette med som standard, og det settes opp med kommandoen:
`virtualenv -p <python_version> /path/to/virtualenv`, f.eks.
`virtualenv -p python3.4 ~/.virtualenvs/koiesys`
Deretter aktiveres det virtuelle miljøet med kommandoen
`source /path/to/virtualenv/bin/activate`
Dersom du gjorde det riktig, vil terminalen din nå si hvilket virtuelle miljø du har aktivert. (F.eks. `(koiesys) user@host $`)

For å deaktivere det virtuelle miljøet, skriv `deactivate`.

### Installasjon av systemet

Dersom du bruker et virtuelt miljø, aktiver det nå.

For å få en oversikt over hva som skjer kommer alle kommandoene til å bli forklart underveis.

- Last ned og pakk ut systemet, og navigèr inn i prosjektmappen.
-
- `pip install -r requirements.txt`
 - Dette installerer alle dependencies for systemet.
- Gå inn i "koieadmin"-mappen. (`cd koieadmin/`)
 - Selve systemet lever i denne mappen.
- Kopier `koieadmin.settings.example-local` til `koieadmin.settings.local` og gjør nødvendige endringer.
- `python manage.py migrate`
 - Setter opp databasen
- `python manage.py createsuperuser`
 - Interaktiv oppsett av  administratorbruker
- `python manage.py import_new_koies`
 - Et script som importerer alle (nye) koier
- `python manage.py import_reservations`
 - Import av tidligere reservasjoner. NB! Les seksjonen for dette før du importerer.
- `python manage.py runserver [ip[:port]]`
 - Dette starter en utviklerversjon av serveren. Du kan nå navigere til ip-adressen som terminalen spytter ut og teste systemet. All navigasjon foregår i menyene på toppen av siden.

## Requirements

We use Celery for queueing of tasks. Make sure to install a broker, e.g. RabbitMQ to actually do the tasks queued. Things will probably still work as expected, but you won't get all functionality.

## Python

Last ned og installer Python 3.4.
`pip install -r requirements.txt`

Dersom dere driver med mye annet python-ish på fritiden bure dere se på virtualenvs.

[How to work on this project!](https://github.com/sklirg/it1901/wiki/How-to-work-on-this-project)
