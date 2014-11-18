from django.db import models
from django.contrib.auth.models import User
from datetime import date

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse


class Facility(models.Model):
    """ Facility class
        Used for creating a facility which can be connected to a koie.
    """
    facility = models.CharField(_('facility'), max_length=50)
    info = models.TextField(_('description'), blank=True, null=True)

    class Meta:
        verbose_name = _('facility')
        verbose_name_plural = _('facilities')

    def __str__(self):
        return self.facility


class Koie(models.Model):
    """ Koie class
        Contains basic information about a koie.
    """
    name = models.CharField(_('koie name'), max_length=50)
    address = models.CharField(_('koie address'), max_length=200)
    location = models.CharField(_('location'), max_length=50)
    latitude = models.DecimalField(_('latitude'), max_digits=10, decimal_places=5)
    longitude = models.DecimalField(_('longitude'), max_digits=10, decimal_places=5)
    num_beds = models.IntegerField(_('beds'), default=0)
    facilities = models.ManyToManyField(Facility, verbose_name=_('facilities'), blank=True, null=True)

    class Meta:
        verbose_name = _('koie')
        verbose_name_plural = _('koies')

    def __str__(self):
        return self.name

    def firewood_capacity(self):
        return self.num_beds * 2

    def needs_refill(self):
        # Error codes:
        # 0 Needs refill
        # 1 OK
        # 2 Soon needs refill
        # 9 No data
        try:
            firewood_status = Report.objects.filter(reservation__koie_ordered=self).order_by('-reported_date')[0].firewood_status
        except:
            return True
        if Report.objects.filter(reservation__koie_ordered=self).count() == 0 or firewood_status is None:
            return True
        else:
            if firewood_status > 15:
                # return 1
                return False
            elif firewood_status > 10:
                # return 2
                return False
            elif firewood_status > 5:
                # return 0
                return False
            else:
                if self.firewood_capacity() < 10:
                    return firewood_status < (self.firewood_capacity() / 2)
                return True

    def get_free_beds(self, date):
        res = Reservation.objects.filter(koie_ordered=self, rent_date=date)
        beds = 0
        for r in res.all():
            beds += r.beds
        return self.num_beds - beds


class Reservation(models.Model):
    """ Reservation class
        Reservation of a koie
    """
    ordered_by = models.ForeignKey(User, verbose_name=_('ordered by'))
    koie_ordered = models.ForeignKey(Koie, verbose_name=_('koie'))
    rent_date = models.DateField(_('rent date'))
    ordered_date = models.DateTimeField(_('reservation registered'), auto_now_add=True)
    beds = models.IntegerField(_('number of beds'))

    class Meta:
        verbose_name = _('reservation')
        verbose_name_plural = _('reservations')
        get_latest_by = 'id'

    def __str__(self):
        return "%(koie)s @ %(date)s" % {'koie': self.koie_ordered, 'date': self.rent_date}
        #return "%s by %s @ %s" % (self.koie_ordered, self.ordered_by, self.rent_date.strftime("%d-%m-%Y"))

    def get_free_beds(self):
        return self.koie_ordered.get_free_beds(self.rent_date)


class Notification(models.Model):
    """ Notification class
        A message you can connect to a koie/reservation.
    """
    koie = models.ForeignKey(Koie, verbose_name=_('koie'))
    due_date = models.DateField(_('due date'))
    message = models.TextField(_('message'), max_length=3000)
    reservation = models.ForeignKey(Reservation, verbose_name=_('reservation'), blank=True, null=True)

    class Meta:
        verbose_name = _('notification')
        verbose_name_plural = _('notifications')

    def __str__(self):
        if len(self.message) > 20:
            message = self.message[:17] + "..."
        else:
            message = self.message
        return "'%s' (%s) " % (message, self.koie)

    def create(self, due_date):
        reservations = Reservation.objects.filter(koie_ordered=self.koie, rent_date__gte=date.today()).exclude(rent_date__lte=self.due_date).order_by('rent_date')
        if reservations.count() > 0:
            best = reservations[0]
        else:
            best = None
        # If the same people reserve a koie for multiple days, this could be bad.
        if best != None:
            self.reservation = best
            self.save()
        return self
        # Some notification if reservation not set?


class Report(models.Model):
    """ Report class
        A report to fill out after a customers stay at a koie
    """
    reservation = models.ForeignKey(Reservation, verbose_name=_('reservation'))
    report = models.TextField(_('comments about your stay'), null=True)
    reported_date = models.DateTimeField(_('reported date'), blank=True, null=True)
    read_date = models.DateTimeField(_('report read date'), blank=True, null=True)
    notification_date = models.DateField(_('notification sent date'), auto_now=True)
    firewood_status = models.IntegerField(_('firewood status'), null=True)

    class Meta:
        verbose_name = _('report')
        verbose_name_plural = _('reports')
        get_latest_by = 'reported_date'

    def submit(self, rep, num):
        self.report = rep
        self.firewood_status = num
        self.save()

    def reported(self):
        return self.reported_date != None

    def read(self):
        return self.read_date != None

    def notified(self):
        return self.notification_date == date.today()

    def get_reservation(self):
        return self.reservation

    def get_absolute_url(self):
        return reverse("koie.views.report_koie", args=[self.id])

    def __str__(self):
        return "%s for %s" % (_('report').capitalize(), self.reservation)

class Damage(models.Model):
    """ Damage class
        A damage on a koie or its equipment
    """
    report = models.ForeignKey(Report, verbose_name=_('report'), blank=True, null=True)
    damaged_koie = models.ForeignKey(Koie, verbose_name=_('damaged koie'), blank=True, null=True)
    damage = models.TextField(_('damage'), blank=True, null=True)
    importance = models.IntegerField(_('importance'), blank=True, null=True)
    fixed_date = models.DateTimeField(_('fixed date'), blank=True, null=True)

    class Meta:
        verbose_name = _('damage')
        verbose_name_plural = _('damages')

    def __str__(self):
        return "%s (@%s)" % (self.damage, self.damaged_koie)

class Firewood(models.Model):
    """ Firewood class
        A OTO relation for firewood status
    """
    koie = models.OneToOneField(Koie, verbose_name=_('koie'))
    firewood_status = models.IntegerField(_('firewood status'), blank=True, null=True)

    def __str__(self):
        return 'Firewood status for %(koie)s: %(status)s' % {'koie': self.koie, 'status': self.firewood_status}

    def get_firewood(self):
        return self.firewood_status

    def get_capacity(self):
        return self.koie.firewood_capacity()

    def get_status(self):
        if self.firewood_status is None:
            return _('N/A')
        return "%s/%s" % (self.firewood_status, self.get_capacity())

    def get_status_code(self):
        if self.firewood_status is None:
            return 2
        if self.get_capacity() > 5:
            if self.firewood_status > 5:
                return 1
            else:
                return 3
        else:
            if self.firewood_status < (self.get_capacity() / 2):
                return 3
            else:
                return 1

    def get_status_class(self):
        if self.firewood_status is None:
            return 'warning'
        if self.get_capacity() > 5:
            if self.firewood_status > 5:
                return 'success'
            else:
                return 'danger'
        else:
            if self.firewood_status < (self.get_capacity() / 2):
                return 'danger'
            else:
                return 'success'

    def get_status_text(self):
        if self.firewood_status is None:
            return _('No information available')
        if self.get_capacity() > 5:
            if self.firewood_status > 5:
                return _('Firewood status OK')
            else:
                return _('Needs refill')
        else:
            if self.firewood_status < (self.get_capacity() / 2):
                return _('Needs refill')
            else:
                return _('Firewood status OK')
