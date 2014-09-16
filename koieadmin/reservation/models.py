from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from koie.models import Koie

class Reservation(models.Model):
    ordered_by = models.ForeignKey(User, related_name=_("ordered by"))
    koie_ordered = models.ForeignKey(Koie, related_name=_("ordered koie"))
    rent_start = models.DateField(_('rent start'))
    rent_end = models.DateField(_('rent end'))
    ordered_date = models.DateTimeField(_('timestamp for order'), auto_now_add=True) # @TODO Exclude from forms

    def __str__(self):
        return "%s by %s @ %s" % (self.koie_ordered, self.ordered_by, self.rent_start.strftime("%d-%m-%Y"))
