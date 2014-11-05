from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import IntegerField, Model


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

    def get_free_beds(self, date):
        res = Reservation.objects.filter(koie_ordered=self, rent_date=date)
        beds = 0
        for r in res.all():
            beds += r.beds
        return self.num_beds - beds

class Reservation(models.Model):
    ordered_by = models.ForeignKey(User, related_name=_("ordered by"))
    koie_ordered = models.ForeignKey(Koie, related_name=_("ordered koie"))
    rent_date = models.DateField(_('rent date'))
    ordered_date = models.DateTimeField(_('timestamp for order'), auto_now_add=True) # @TODO Exclude from forms
    beds = models.IntegerField(_('number of beds'))

    class Meta:
        get_latest_by = 'id'

    def __str__(self):
        return "%s by %s @ %s" % (self.koie_ordered, self.ordered_by, self.rent_date.strftime("%d-%m-%Y"))

    def get_free_beds(self):
        return self.koie_ordered.get_free_beds(self.rent_date)

class Report(models.Model):
    reservation = models.ForeignKey(Reservation, related_name=_("reservation"))
    report = models.TextField(_('end of stay report'))
    reported_date = models.DateTimeField(blank=True, null=True)
    read_date = models.DateTimeField(blank=True, null=True)
    firewood_status = models.IntegerField()

    def submit(self, rep, num):
        self.report = rep
        self.firewood_status = num
        self.save()

    def reported(self):
        return self.reported_date != None

    def read(self):
        return self.read_date != None

    def get_reservation(self):
        return self.reservation

    def __str__(self):
        return "Report for %s" % self.reservation

    class Meta:
        get_latest_by = 'reported_date'

class Damage(models.Model):
    reporten = models.ForeignKey(Report, related_name=_("reporten"), blank=True, null=True)
    damaged_koie = models.ForeignKey(Koie, related_name=_("damaged_koie"), blank=True, null=True)
    damage = models.TextField(_('skade'), blank=True, null=True)
    importance = models.IntegerField(blank=True, null=True)
    fixed_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "%s (@%s)" % (self.damage, self.damaged_koie)
        
class Facility(models.Model):
    koier = models.ManyToManyField(Koie, related_name=_('koier'), blank=True, null=True)
    facility = models.CharField(_('facility name'), max_length=50)
    info = models.TextField(_('facility info'), blank=True, null=True)
    
    def __str__(self):
        return self.facility
