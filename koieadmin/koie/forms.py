from django import forms
from django.forms import ModelForm
from koie.models import Reservation, Report, Damage

class ReservationForm(ModelForm):
    email = forms.EmailField(label='Your email', max_length=100)

    class Meta:
        model = Reservation
        exclude = ('ordered_by', 'ordered_date',)

class ReportForm(ModelForm):
    damages = forms.CharField(label='Her kan eventuelle skader fylles inn. I folgende format: skade -- viktighet --- evt. ny skade')
    class Meta:
        model = Report
        fields = ('report', 'firewood_status', 'damages', )
