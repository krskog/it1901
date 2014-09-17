from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from koie.models import Koie

# Index view: Shows all koies

def index(request):
    koies = Koie.objects.all()
    return render(request, 'index.html', {'koies': koies})

def koie_detail(request, koie_id):
    koie = get_object_or_404(Koie, pk=koie_id)
    return render(request, 'koie.html', {'koie': koie})
