from django import forms
from django.forms import ModelForm, Form
from koie.models import Reservation, Report, Damage
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin.widgets import AdminDateWidget
from datetime import date, datetime

class ReservationForm(ModelForm):
    email = forms.EmailField(label='Your email', max_length=100)
    rente_date = forms.DateField(widget=SelectDateWidget, initial=date.today())
   
    class Meta:
        model = Reservation
        exclude = ('ordered_by', 'ordered_date', 'rent_date' ,)

class ReportForm(ModelForm):
    damages = forms.CharField(label='Her kan eventuelle skader fylles inn. I folgende format: skade1 -- skade2 -- skade3...')
    class Meta:
        model = Report
        fields = ('report', 'firewood_status', 'damages', )

class DamageForm(ModelForm):
    
    class Meta:
        model = Damage
        fields = ('importance', 'fixed_date', )
