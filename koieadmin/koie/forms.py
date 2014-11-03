from django import forms
from django.forms import ModelForm
from koie.models import Reservation, Report, Damage

class ReservationForm(ModelForm):
    email = forms.EmailField(label='Your email', max_length=100)

    class Meta:
        model = Reservation
        exclude = ('ordered_by', 'ordered_date',)

class ReportForm(ModelForm):
    damages = forms.CharField(label='Her kan eventuelle skader fylles inn. I folgende format: skade1 -- skade2 -- skade3...', required=False)
    class Meta:
        model = Report
        fields = ('report', 'firewood_status', 'damages',)


class GetReportsForm(forms.Form):
    email = forms.EmailField(label='Your email', max_length=100)

    class Meta:
        name = 'get reports'


# This is the admin form
class DamageForm(ModelForm):
    class Meta:
        model = Damage
        fields = ('importance', 'fixed_date', )
