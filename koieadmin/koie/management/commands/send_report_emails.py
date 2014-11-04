#### WARNING - MAKE SURE YOU SOURCE VIRTUALENV !
from django.core.management.base import BaseCommand, CommandError
from koie.models import Koie, Reservation, Report
from koie.views import send_report_email

from datetime import date, timedelta

class Command(BaseCommand):
    args = ""
    help = "Send reports to all users who just had a stay"

    def handle(self, *args, **options):
        mails_to_send = 0
        already_notified = 0

        #todays_reservations = Reservation.objects.filter(rent_date__lte=date.today())
        todays_reports = Report.objects.filter(reservation__rent_date__lte=date.today() + timedelta(1), reported_date=None)

        for report in todays_reports:
            send_report_email({}, report.id)
