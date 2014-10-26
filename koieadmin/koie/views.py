from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _

from datetime import date, datetime

from django.contrib.auth.models import User
from koie.models import Koie, Reservation, Report
from koie.forms import ReservationForm, ReportForm, ReadForm
from django.core.mail import send_mail

# Index view: Shows all koies

def index(request):
    return render(request, 'index.html', {
      'active': 'index',
      'breadcrumbs': [
          {'name': _('home').capitalize()}
      ]
    })

def koie_index(request):
    koies = Koie.objects.all()
    return render(request, 'koies.html', {
      'active': 'koie_index',
      'breadcrumbs': [
          {'name': _('home').capitalize(), 'url': 'index'},
          {'name': _('koier').capitalize()}
      ],
      'koies': koies
    })

def koie_detail(request, koie_id):
    koie = get_object_or_404(Koie, pk=koie_id)
    return render(request, 'koie_detail.html', {
      'active': 'koie_detail',
      'breadcrumbs': [
          {'name': _('home').capitalize(), 'url': 'index'},
          {'name': _('koier').capitalize(), 'url':'koie_index'},
          {'name': koie.name}
      ],
      'koie': koie,
      'future_reservations': get_future_reservations(koie),
      #'free_beds': koie.free_beds(reservation.rent_date)
    })

def next_reservations(request):
    return render(request, 'next_reservations.html', {
      'active': 'next_reservations',
      'future_reservations': get_future_reservations(num=25),
      'breadcrumbs': [
          {'name': _('home'), 'url': 'index'},
          {'name': _('next reservations')}
      ],
    })

def latest_reports(request):
    return render(request, 'latest_reports.html', {
      'active': 'next_reservations',
      'latest_reports': get_latest_reports(),
      'breadcrumbs': [
          {'name': _('home'), 'url': 'index'},
          {'name': _('latest reports')}
      ],
    })

def get_report(request, report_id):
	rep = get_object_or_404(Report, pk=report_id)

	if request.method == 'POST':
		form = ReadForm(request.POST)
		if form.is_valid():
			rep.readIt(form.cleaned_data['read'])
			return redirect('latest_reports')
	else:
		form = ReadForm()

	return render(request, 'show_report.html', {
	'active': 'les rapport',
            'reporten': get_specific_report(report_id),
            'koia': get_koia(report_id),
	'breadcrumbs': [
		{'name': _('home'), 'url': 'index'},
                        {'name': _('latest reports'), 'url': 'latest_reports'},
		{'name': _(rep.__str__())}
	],
	'form': form
	})


### Forms & Stuff

def reserve_koie(request, reservation_id=None):
    if reservation_id == None:
        reservation = Reservation()
    else:
        reservation = get_object_or_404(Reservation, pk=reservation_id)

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        # Find user by email or crash
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.ordered_by = get_or_create_user(form.cleaned_data['email'])
            reservation.save()
            send_report_email(reservation) #Sends an email with a link to the report form connected to this reservation
            return redirect('koie_detail', koie_id=reservation.koie_ordered.id) # Redirect to koie page
        else:
            form = ReservationForm(request.POST)
    else:
        form = ReservationForm()

    return render(request, 'reservation.html', {
    'active': 'reserve_koie',
    'breadcrumbs': [
        {'name': _('home').capitalize(), 'url': 'index'},
        {'name': _('reservation').capitalize()}
    ],
    'form': form
    })

def report_koie(request, report_id):
	rep = get_object_or_404(Report, pk=report_id)

	if request.method == 'POST':
		form = ReportForm(request.POST)
		if form.is_valid():
			rep.submit(form.cleaned_data['report'], form.cleaned_data['firewood_status'])
			return redirect('index')
	else:
		form = ReportForm()

	return render(request, 'report.html', {
	'active': 'report_koie',
	'breadcrumbs': [
		{'name': _('home').capitalize(), 'url': 'index'},
		{'name': rep}
	],
	'form': form
	})


## ========== METHODS =============

### Validation

def get_or_create_user(email):
    users = User.objects.filter(email=email)
    if users.count() > 1:
        pass # WHAT THE FUCK
    elif users.count() == 1:
        return users[0]
    else:
       # Create new user
        user = User()
        user.email = email
        user.username = email
        user.save()
        return user

### Lists / views

def get_future_reservations(koie=None, num=10):
    today = date.today()
    if koie == None:
        return Reservation.objects.filter(rent_date__gte=today).order_by('rent_date')[:num]
    else:
        return Reservation.objects.filter(koie_ordered=koie, rent_date__gte=today).order_by('rent_date')[:num]


### Latest reports

def get_latest_reports():
    return Report.objects.filter(read=False)

def get_specific_report(id):
    return Report.objects.filter(id = id)

def get_koia(id):
    repid =  Report.objects.get(id = id)
    resid =  Reservation.objects.get(id = repid.reservation_id)
    koie = Koie.objects.get(id = resid.koie_ordered_id)
    return koie.name



### Mailing

def send_report_email(reservation):
	report = Report()
	report.reservation = reservation
	report.submit('', 0)
	recipient = reservation.ordered_by.email
	message = 'Please fill out a report for your stay at: http://127.0.0.1:8000/report/' + str(report.id) + '/'
	send_mail('Report for koie', message, 'ntnu.koier@gmail.no', [recipient])
