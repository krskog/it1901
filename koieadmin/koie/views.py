from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from django.utils.translation import ugettext_lazy as _

from koie.models import Koie

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
    return render(request, 'koie_detail.html', {
      'active': 'koie_detail',
      'breadcrumbs': [
          {'name': _('home'), 'url': 'index'},
          {'name': _('koier'), 'url':'koie_index'},
          {'name': koie.name}
      ],
      'koie': koie,
    })
