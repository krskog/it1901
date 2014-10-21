from django import forms
from django.forms import ModelForm
from koie.models import Reservation, Report

class ReservationForm(ModelForm):
    email = forms.EmailField(label='Your email', max_length=100)

    class Meta:
        model = Reservation
        exclude = ('ordered_by', 'ordered_date',)
		
class ReportForm(ModelForm):
	
	class Meta:
		model = Report
		fields = ('report', 'firewood_status')
