from django import forms
from django.forms import ModelForm
from koie.models import Reservation, Report, Damage, Notification
from django.utils.translation import ugettext_lazy as _

from django.forms.extras.widgets import SelectDateWidget
from datetime import date

class ReservationForm(ModelForm):
    name = _('reservation form')

    email = forms.EmailField(label=_('Your email'), max_length=100)
    rent_date = forms.DateField(label=_("Rent date"), widget=SelectDateWidget, initial=date.today())

    class Meta:
        model = Reservation
        exclude = ('ordered_by', 'ordered_date',)


class ReportForm(ModelForm):
    name = _('report form')

    damages = forms.CharField(label='damages; write each damage on its own line', widget=forms.Textarea, required=False)
    class Meta:
        model = Report
        fields = ('report', 'firewood_status', 'damages',)


class GetReportsForm(forms.Form):
    name = _('get users reports form')

    email = forms.EmailField(label=_('Your email'), max_length=100)

    class Meta:
        name = 'get reports'


# This is the admin form
class DamageForm(ModelForm):
    name = _('damages form')
    fixed_date = forms.DateField(label=_('Fixed date'), widget=forms.TextInput(attrs={'placeholder': date.today()}), required=False)
    # fixed_date = forms.DateField(label=_("Fixed date"), widget=SelectDateWidget, initial=date.today())
    class Meta:
        model = Damage
        fields = ('importance', 'fixed_date',)


class NotificationForm(ModelForm):
    name = _('notification form')
    due_date = forms.DateField(label='due date', widget=SelectDateWidget, initial=date.today())

    class Meta:
        model = Notification
        fields = ('koie', 'due_date', 'message',)
