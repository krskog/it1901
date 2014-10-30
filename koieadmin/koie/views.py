from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from datetime import date, datetime
from django.contrib.auth.models import User
from django.contrib import messages
from koie.models import Koie, Reservation, Report
from koie.forms import ReservationForm, ReportForm
from django.core.mail import send_mail


# Index view
def index(request):
    return render(request, 'index.html', {
      'active': 'index',
      'breadcrumbs': [
          {'name': _('home').capitalize()}
      ]
    })


# Koie list
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


# Koie detail, lists information about a koie
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
    })


# Lists upcoming reservations
def next_reservations(request):
    return render(request, 'next_reservations.html', {
      'active': 'next_reservations',
      'future_reservations': get_future_reservations(num=25),
      'breadcrumbs': [
          {'name': _('home'), 'url': 'index'},
          {'name': _('next reservations')}
      ],
    })


# Lists latest reports
def latest_reports(request, slug=None):
    # Filters for the report view
    if slug == 'read':
        reports = []
        for r in Report.objects.all():
            print(r, r.read_date)
            if r.read_date is not None:
                reports.append(r)
    elif slug == 'unread':
        reports = []
        for r in Report.objects.all():
            print(r, r.read_date)
            if r.read_date is None:
                reports.append(r)
    elif slug == 'all':
        reports = Report.objects.all()
    elif slug == 'reported':
        reports = []
        for r in Report.objects.all():
            if r.reported_date is not None:
                reports.append(r)
    elif slug == 'unreported':
        reports = []
        for r in Report.objects.all():
            if r.reported_date is None:
                reports.append(r)
    else:
        slug = 'default'
        reports = get_latest_reports()
    return render(request, 'latest_reports.html', {
      'active': 'next_reservations',
      'latest_reports': reports,
      'breadcrumbs': [
          {'name': _('home').capitalize(), 'url': 'index'},
          {'name': _('reports').capitalize(), 'url': 'latest_reports'},
          {'name': slug.capitalize()}
      ],
      'slug': slug,
    })


# A view for admins to read reports
def read_report(request, report_id=None):
    if report_id is None:
        messages.error(request, 'No report specified')
        return redirect(latest_reports)

    report = get_object_or_404(Report, id=report_id)
    if request.method == 'POST':
        print(request.POST)
        # Should mark report as read?
        if request.POST['act'] == 'report_read':
            if request.POST['read-btn'] == 'Lest':
                messages.success(request, 'Report marked as read')
                report.read_date = datetime.now()
                report.save()
                return redirect(latest_reports)

    return render(request, 'show_report.html', {
        'active': 'read_report',
        'breadcrumbs': [
            {'name': _('home').capitalize(), 'url': 'index'},
            {'name': _('reports').capitalize(), 'url': 'latest_reports'},
            {'name': report}
        ],
        'report': report,
    })


### Forms & Stuff
#checks for valid date
def valDal(form):
        reservation = form.save(commit=False)
        rdate = reservation.rent_date
        cdate = date.today()
        if rdate >= cdate:
            return True
        else:
            return False
#checks for valid number of beds
def valBal(form):
        if form.is_valid():
            reservation = form.save(commit=False)
            rbeds = reservation.beds
            fbeds = reservation.get_free_beds()
            if 0 < rbeds and rbeds <= fbeds:
                return True
            else:
                return False

        else:
            return False

def errorMessage(form):
    if not form.is_valid():
        return  'Your email adress is invalid'
    else:
        if not valBal(form):
            return  'Your desired number of bed is not available'
        else:
            if not valDal(form):
                return  'Your desired rent date is invalid'

def reserve_koie(request, reservation_id=None, koie_id=None):
    if reservation_id == None:
        reservation = Reservation()
    else:
        reservation = get_object_or_404(Reservation, pk=reservation_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        # Find user by email or crash
        if valBal(form) and valDal(form):
            reservation = form.save(commit=False)
            reservation.ordered_by = get_or_create_user(form.cleaned_data['email'])
            reservation.save()
            report = send_report_email(reservation)
            messages.success(request, '%s reserved for %s.' % (reservation.koie_ordered, reservation.rent_date))
            messages.info(request, 'You will have to fill out a report after your stay. Please check your email.')
            # Sends an email with a link to the report form connected to this reservation
            # Should be split into report creation and then cronjob email sending
            return redirect('koie_detail', koie_id=reservation.koie_ordered.id) # Redirect to koie page
        else:
            messages.error(request, errorMessage(form))
            form = ReservationForm(request.POST)
    else:
        form = ReservationForm()
        if koie_id is not None:
            koie = get_object_or_404(Koie, id=koie_id)
            form.fields['koie_ordered'].initial = koie

    return render(request, 'reservation.html', {
    'active': 'reserve_koie',
    'breadcrumbs': [
        {'name': _('home').capitalize(), 'url': 'index'},
        {'name': _('reservation').capitalize()}
    ],
    'form': form
    })


def report_koie(request, report_id):
    report = get_object_or_404(Report, pk=report_id)

    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report_clean = form.save(commit=False)
            report_clean.reservation = report.reservation
            print("clean report", report_clean)
            report_clean.reported = datetime.now()
            print("report %s" % report_clean)
            report_clean.save()
            #report.submit(form.cleaned_data['report'], form.cleaned_data['firewood_status'])
            messages.success(request, 'Report submitted')
            return redirect('index')
    else:
        form = ReportForm()

    return render(request, 'report.html', {
    'active': 'report_koie',
    'breadcrumbs': [
        {'name': _('home').capitalize(), 'url': 'index'},
        {'name': report}
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
    return Report.objects.filter(read_date=None)

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
    #report.submit('', 0)
    report.report = ''
    report.firewood_status = 0
    report.save()
    recipient = reservation.ordered_by.email
    message = 'Please fill out a report for your stay at: http://127.0.0.1:8000/report/' + str(report.id) + '/'
    #send_mail('Report for koie', message, 'ntnu.koier@gmail.no', [recipient])
    return report
