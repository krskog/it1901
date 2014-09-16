from django.db import models
from django.utils.translation import ugettext_lazy as _
#from django.contrib.auth.models import User

from koie.models import Koie
from reservation.models import Reservation

class Report(models.Model):
    reservation = models.ForeignKey(Reservation, related_name=_("reservation"))
