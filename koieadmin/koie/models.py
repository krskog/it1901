from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _


class Koie(models.Model):
    name = models.CharField(_('koie name'), max_length=50)
    address = models.CharField(_('koie address'), max_length=200)
    location = models.CharField(_('location'), max_length=50)
    latitude = models.DecimalField(_('latitude'), max_digits=10, decimal_places=5)
    longitude = models.DecimalField(_('longitude'), max_digits=10, decimal_places=5)
    num_beds = models.IntegerField(_('beds'), default=0)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    ordered_by = models.ForeignKey(User, related_name=_("ordered by"))
    koie_ordered = models.ForeignKey(Koie, related_name=_("ordered koie"))
    rent_start = models.DateField(_('rent start'))
    rent_end = models.DateField(_('rent end'))
    ordered_date = models.DateTimeField(_('timestamp for order'), auto_now_add=True) # @TODO Exclude from forms

    def __str__(self):
        return "%s by %s @ %s" % (self.koie_ordered, self.ordered_by, self.rent_start.strftime("%d-%m-%Y"))

class Report(models.Model):
    reservation = models.ForeignKey(Reservation, related_name=_("reservation"))
    report = models.TextField(_('end of stay report'))
    reported_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Report for %s" % self.reservation
