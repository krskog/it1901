from django import forms
from django.forms import ModelForm
from koie.models import Reservation

class ReservationForm(ModelForm):
    email = forms.EmailField(label='Your email', max_length=100)

    class Meta:
        model = Reservation
        exclude = ('ordered_by', 'ordered_date',)
