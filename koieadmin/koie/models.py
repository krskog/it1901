from django.db import models
from django.utils.translation import ugettext_lazy as _

class Koie(models.Model):
    name = models.CharField(_('koie name'), max_length=50)
    address = models.CharField(_('koie address'), max_length=200)
    zip_code = models.IntegerField(_('zip code'), max_length=4)
    location = models.CharField(_('location'), max_length=50)
    num_beds = models.IntegerField(_('beds'), default=0)

    def __str__(self):
        return self.name

    def get_address(self):
        return "%s %s, %s %s" % (self.address, self.house_no, self.zip_code, self.location)
