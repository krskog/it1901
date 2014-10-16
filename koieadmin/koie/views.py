from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _

from datetime import date, datetime

from django.contrib.auth.models import User
from koie.models import Koie, Reservation, Report
from koie.forms import ReservationForm

# Index view: Shows all koies

def index(request):
    return render(request, 'index.html', {
      'active': 'index',
      'breadcrumbs': [
          {'name': _('home')}
      ]
    })

def koie_index(request):
    koies = Koie.objects.all()
    for koie in koies:
        koie.is_reserved = is_koie_reserved(koie)
    return render(request, 'koies.html', {
      'active': 'koie_index',
      'breadcrumbs': [
          {'name': _('home'), 'url': 'index'},
          {'name': _('koier')}
      ],
      'koies': koies
    })

def koie_detail(request, koie_id):
    koie = get_object_or_404(Koie, pk=koie_id)
    koie.is_reserved = is_koie_reserved(koie)
    return render(request, 'koie_detail.html', {
      'active': 'koie_detail',
      'breadcrumbs': [
          {'name': _('home'), 'url': 'index'},
          {'name': _('koier'), 'url':'koie_index'},
          {'name': koie.name}
      ],
      'koie': koie,
      'future_reservations': list_future_reservations(koie),
      #'free_beds': koie.free_beds(reservation.rent_start)
    })

def next_reservations(request):
    return render(request, 'next_reservations.html', {
      'active': 'next_reservations',
      'future_reservations': list_next_reservations(25),
    })

### Forms & Stuff

def reserve_koie(request, reservation_id=None):
    if reservation_id == None:
        reservation = Reservation()
    else:
        reservation = get_object_or_404(Reservation, pk=reservation_id)
    # Some form stuff

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        # Find user by email or crash
        print("form pre validation\n%s" % form)
        if form.is_valid():
            print("form.cleaned %s" % form.cleaned_data)
            reservation = form.save(commit=False)
            reservation.ordered_by = get_or_create_user(form.cleaned_data['email'])
            print("reservation %s" % reservation)
            reservation.save()
            return redirect('/') # Redirect to koie page
    else:
        form = ReservationForm()

    return render(request, 'reservation.html', {'form': form})


## ========== METHODS =============

### Validation

def is_koie_reserved(koie):
    now = date.today()
    reservation_set = Reservation.objects.filter(koie_ordered=koie)
    for reservation in reservation_set:
        if now > reservation.rent_start and now < reservation.rent_end:
            return (reservation.rent_start, reservation.rent_end)

    return False #now > koie.rent_start and now < koie.rent_end

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

def list_future_reservations(koie):
    reservations = Reservation.objects.filter(koie_ordered=koie).order_by('rent_start')
    future = []
    for r in reservations.all():
        if r.rent_start > date.today():
            r.free_beds = r.koie_ordered.free_beds(r.rent_start)
            future.append(r)
    return future

def list_next_reservations(number):
    reservations = Reservation.objects.order_by('rent_start')
    nextRes = []
    for r in reservations.all():
        if r.rent_start > date.today():
            r.free_beds = r.koie_ordered.free_beds(r.rent_start)
            nextRes.append(r)
        if (len(nextRes) == number):
            break
    return nextRes
