import datetime

from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpRequest
from .forms import *
from .models import *
def home(request:HttpRequest):
    form=SearchForm(request.POST or None)

    if form.is_valid():
        rijec=form.cleaned_data['Naziv_konkursa']
        print(rijec)
        tip=form.cleaned_data['tip']
        print(tip)
        danas = datetime.date.today()
        konkursi=Konkurs.objects.filter(naziv__contains=rijec).filter(tip__in=tip).filter(datum_otvaranja__lte=danas).filter(datum_zatvaranja__gte=danas)
        formica = VestForm(request.POST or None)

        context = {
            'konkursi': konkursi,
            'formica':formica
        }

        return render(request, 'jobfair/pretraga.html', context)
    context={
        'form':form,
    }
    return render(request,'jobfair/home.html',context)

