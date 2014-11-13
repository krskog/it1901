from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext_lazy as _
from datetime import date, datetime, timedelta
from django.contrib.auth.models import User
from django.contrib import messages
from koie.models import Koie, Reservation, Report, Damage, Facility, Notification
from koie.forms import ReservationForm, ReportForm, DamageForm, GetReportsForm, NotificationForm
from django.core.mail import send_mail
from koieadmin import settings

# Index view
def index(request):
    koies = Koie.objects.all()
    return render(request, 'index.html', {
      'active': 'index',
      'breadcrumbs': [
          {'name': _('home').capitalize()}
      ],
      'koies': koies,
    })


# Koie list
def koie_index(request):
    koies = Koie.objects.all()
    if request.user.is_authenticated():
        for koie in koies:
            koie.unread_reports = Report.objects.filter(reservation__koie_ordered=koie, read_date=None).exclude(reported_date=None).count()
            if Report.objects.filter(reservation__koie_ordered=koie).count() >= 1:
                koie.firewood = Report.objects.filter(reservation__koie_ordered=koie).latest('reported_date').firewood_status
            else:
                koie.firewood = 'N/A'
            koie.damages = Damage.objects.filter(damaged_koie=koie, fixed_date=None).count()
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


# Lists damages
def get_damages(request, slug=None):
    # Filters for the damage view
    if slug == 'fixed':
        damages = Damage.objects.exclude(fixed_date=None).order_by('-importance')
    elif slug == 'not_fixed':
        damages = Damage.objects.filter(fixed_date=None).order_by('-importance')
    else:
        slug = 'default'
        damages = get_latest_damages()
    return render(request, 'damages.html', {
      'active': 'damages',
      'damages': damages,
      'breadcrumbs': [
          {'name': _('home').capitalize(), 'url': 'index'},
          {'name': _('damages').capitalize(), 'url': 'damages'},
          {'name': slug.capitalize()}
      ],
      'slug': slug,
    })

# A view for admins to read reports
def damage_fixed(request, damage_id=None):
    if damage_id is None:
        messages.error(request, 'No report specified')
        return redirect(get_damages)

    damage = get_object_or_404(Damage, id=damage_id)
    damage.fixed_date = datetime.now()
    damage.save()
    return redirect(get_damages)


def edit_damage(request, damage_id):
    damage = get_object_or_404(Damage, pk=damage_id)
    if request.method == 'POST':
        form = DamageForm(request.POST, instance=damage)
        if form.is_valid():
            damage_clean = form.save(commit=False)
            damage.importance = damage_clean.importance
            if not damage_clean.fixed_date == None:
                damage.fixed_date = damage_clean.fixed_date
            damage.save()
            messages.success(request, 'Damage edited')
            return redirect(get_damages)
    else:
        form = DamageForm(instance=damage)

    return render(request, 'damage_importance.html', {
    'active': 'damagen',
    'damagen': damage,
    'breadcrumbs': [
        {'name': _('home').capitalize(), 'url': 'index'},
          {'name': _('damages').capitalize(), 'url': 'damages'},
          {'name': _('edit damages')},
    ],
    'form': form
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

def reserve_koie(request, reservation_id=None, koie_id=None):
    if reservation_id == None:
        reservation = Reservation()
    else:
        reservation = get_object_or_404(Reservation, pk=reservation_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.ordered_by = get_or_create_user(form.cleaned_data['email'])
            if validate_reservation(request, reservation):
                reservation.save()
                report = generate_report(reservation)
                messages.success(request, _('%(koie)s reserved for %(date)s.' % {'koie': reservation.koie_ordered, 'date': reservation.rent_date}))
                messages.info(request, _('You will have to fill out a report after your stay. Please check your email.'))
                send_report_email(report)
                # Sends an email with a link to the report form connected to this reservation
                # Should be split into report creation and then cronjob email sending
                return redirect('koie_detail', koie_id=reservation.koie_ordered.id) # Redirect to koie page
            else:
                form = ReservationForm(request.POST)
        else:
            messages.error(request, _('Invalid email address'))
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


def notification_index(request):
    notifications = Notification.objects.all()
    return render(request, 'notifications.html', {
        'active': 'notification_index',
        'breadcrumbs': [
            {'name': _('home').capitalize(), 'url': 'index'},
            {'name': _('notifications').capitalize()}
        ],
        'notifications': notifications,
    })


def create_notification(request, koie_id=None):
    if koie_id != None:
        koie = get_object_or_404(Koie, pk=koie_id)
    else:
        koie = None
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            # notification = form.cleaned_data
            notification = form.save()
            due_date = form.cleaned_data['due_date']
            notification = notification.create(due_date)
            if notification.reservation != None:
                messages.success(request, _('Added notification to %s' % notification.reservation))
            else:
                messages.warning(request, _('Created notification, but did not find any reservations to notify.'))
        else:
            messages.error(request, _('Something failed, please try again later.'))
    else:
        form = NotificationForm()
        if koie is not None:
            form.fields['koie'].initial = koie
    return render(request, 'notification_form.html', {
        'active': 'create_notification',
        'breadcrumbs': [
            {'name': _('home').capitalize(), 'url': 'index'},
            {'name': _('create notification').capitalize()}
        ],
        'form': form,
    })


def report_koie(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    if request.method == 'POST':
        form = ReportForm(request.POST, instance=report)
        if form.is_valid():
            report_clean = form.save(commit=False)
            report_clean.reservation = report.reservation
            report_clean.reported_date = datetime.now()
            damages = str(form.cleaned_data['damages'] )
            report_clean.save()
            reportDamage(damages, report_clean)
            messages.success(request, _('Report submitted'))
            return redirect('index')
        else:
            messages.error(request, _("Did you fill out all the fields?"))
    else:
        form = ReportForm(instance=report)

    return render(request, 'report.html', {
    'active': 'report_koie',
    'breadcrumbs': [
        {'name': _('home').capitalize(), 'url': 'index'},
        {'name': report}
    ],
    'form': form
    })

def my_reports(request, email=None):
    if request.method == 'POST':
        form = GetReportsForm(request.POST)
        if form.is_valid() and email is None:
            email = form.cleaned_data['email']
        user = get_or_create_user(email)
        reports = Report.objects.filter(reservation__ordered_by=user, reported_date=None)
        if reports.count() == 0:
            messages.success(request, _("You have no unreported stays."))
            return redirect(index)
        elif reports.count() == 1:
            return redirect(report_koie, reports[0].id)
        else:
            messages.success(request, _("You have more than one report to fill out. Here is the first one."))
            return redirect(report_koie, reports[0].id)
    else:
        form = GetReportsForm()
        return render(request, 'get_unreported_reports.html', {
            'active': 'get_unreported_reports',
            'breadcrumbs': [
                {'name': _('home').capitalize(), 'url': 'index'},
                {'name': _('get reports').capitalize()},
            ],
            'form': form,
        })

class Vedstatus:
    def init(self, ved, seng):
        self.ved = ved
        self.vedkapasitet = int(seng)*2
        if ved < 6:
            self.status = _('Needs refill')
        else:
            self.status = _('Firewood status is OK')


def firewood_status(request):
    koies = Koie.objects.all()
    for koie in koies:
        print(koie, koie.needs_refill())
        #koie.unread_reports = Report.objects.filter(reservation__koie_ordered=koie, read_date=None).exclude(reported_date=None).count()
        if Report.objects.filter(reservation__koie_ordered=koie).count() >= 1:
            koie.firewood = Report.objects.filter(reservation__koie_ordered=koie).latest('reported_date').firewood_status
        else:
            koie.firewood = -1

    return render(request, 'firewood.html', {
    'active': 'koies',
    'koies': koies,
    'breadcrumbs': [
    {'name': _('home').capitalize(), 'url': 'index'},
    {'name': _('firewood status').capitalize()},
        ],
    })

# This should be rewritten to use newlines instead.
def reportDamage(tekst, report):
    if '\n' in tekst:
        tdamages = tekst.split('\n')
        num_damages = len(tdamages)
        for n in range(0, num_damages):
            reported_damage = tdamages[n].strip()
            if 3 < len(reported_damage):
                damage = Damage()
                damage.damage = reported_damage
                damage.report = report
                damage.damaged_koie = report.reservation.koie_ordered
                damage.save()
    else:
        damage = Damage()
        damage.damage = tekst
        damage.reporten = report
        damage.damaged_koie = report.reservation.koie_ordered
        damage.save()

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

def get_latest_damages():
    return Damage.objects.filter(fixed_date=None).order_by('-importance')

def get_latest_reports():
    return Report.objects.filter(read_date=None)

def get_specific_report(id):
    return Report.objects.filter(id = id)

def get_koia(id):
    repid =  Report.objects.get(id = id)
    resid =  Reservation.objects.get(id = repid.reservation_id)
    koie = Koie.objects.get(id = resid.koie_ordered_id)
    return koie.name

def get_koi(report_id):
    repid =  Report.objects.get(id = report_id)
    resid =  Reservation.objects.get(id = repid.reservation_id)
    koie = Koie.objects.get(id = resid.koie_ordered_id)
    return koie


# Mailing
def send_report_email(report):
    #if report_id is None:
    #    report_id = report.id
    #    report = get_object_or_404(Report, pk=report_id)
    report.save()  # Marks as edited, updates sent notification-field
    recipient = report.reservation.ordered_by.email
    url = "%s%s" % (settings.BASE_URL, report.get_absolute_url())
    message = _('Please fill out a report for your stay at: %s' % url)
    send_mail('Report for koie', message, settings.EMAIL_HOST_USER, [recipient])
    #return redirect(latest_reports)


def send_notification_email(notification):
    equipment = notification.message
    message = '\
        Hei! Det har nå blitt koblet en utstyrsmelding opp mot din reservasjon for %(koie)s den %(res_date)s.\n\
        Du skal ta med deg:\n\
        %(equipment)s\n\
        \n\
        Dersom du har spørsmål angående utstyrsmeldingen, kontakt oss.\n\n\
        Mvh,\n\
        Koieadministrasjonssystemet\
        ' \
        % {'koie': notification.koie, 'date': notification.reservation.rent_date, 'equipment': equipment}
    recipient = notification.reservation.ordered_by.email
    send_email('Utstyrsmelding', message, settings.EMAIL_HOST_USER, [recipient])


def send_email(topic, message, fr, to):
    send_mail(topic, message, fr, to)


def generate_report(reservation):
    report = Report()
    report.reservation = reservation
    report.save()
    return report


# Validates reservation
def validate_reservation(request, reservation):
    if not validate_date(request, reservation.rent_date):
        return False
    elif not validate_reserved_beds(reservation.koie_ordered, reservation.beds):
        messages.error(request, _('Invalid number of beds'))
        return False
    else:
        return True


# Validates date
def validate_date(request, date):
    if date < date.today():
        messages.error(request, _('You cannot reserve for the past'))
        return False
    elif date > (date.today() + timedelta(3 * 30)):
        messages.error(request, _('You cannot reserve for more than 3 months in the future'))
        return False
    else:
        return True

# Validates number of beds
def validate_reserved_beds(koie, num_beds):
    return num_beds > 0 and num_beds <= koie.num_beds
