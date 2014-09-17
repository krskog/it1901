from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from koie.models import Koie

# Index view: Shows all koies

def index(request):
    return render(request, 'index.html', {'active': 'index'})

def koie_index(request):
    koies = Koie.objects.all()
    return render(request, 'koies.html', {'koies': koies, 'active': 'koie_index'})

def koie_detail(request, koie_id):
    koie = get_object_or_404(Koie, pk=koie_id)
    return render(request, 'koie_detail.html', {'koie': koie, 'active': 'koie_detail'})
