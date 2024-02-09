from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.http import  HttpRequest
from .forms import *
from .models import *
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

from django.contrib.auth.decorators import login_required,permission_required
def index(reqest: HttpRequest):
    form = SearchForm(reqest.POST or None)

    if form.is_valid():
        term=form.cleaned_data['term']
        vijesti=Vijest.objects.filter(sadrzaj__contains=term)
    else:

        vijesti=Vijest.objects.order_by('-timestamp')
    context={
        'form': form,
        'vijesti':vijesti,
        'vijestform':VijestForm()
    }
    return render(reqest,'vijesti/index.html',context)
@login_required(login_url='login')
def creatingVijest(request: HttpRequest):
    form=VijestForm(request.POST or None)
    if form.is_valid():
        vijest=form.save(commit=False)
        vijest.autor=Korisnik.objects.get(username=request.user.get_username())
        vijest.save()
    return redirect('home')

@login_required(login_url='login')
@permission_required('vijesti.delete_vijest',raise_exception=True)
def deleteVijest(request: HttpRequest):
    vijestid=request.POST.get('vijestid')
    if vijestid:
        vijest=Vijest.objects.get(pk=vijestid)
        if vijest.autor==request.user or request.user.has_perm('vijesti.delete_vijest'):
            vijest.delete()
    return redirect('home')


def login_req(request: HttpRequest):
    form= AuthenticationForm(request=request,data=request.POST or None)
    if form.is_valid():
        user=form.cleaned_data['username']
        password=form.cleaned_data['password']
        user=authenticate(username=user,password=password)
        print(user,password)
        if user:
            login(request,user)
            messages.info(request,"Uspjesan login")
            return redirect('home')
    else:
        messages.error(request, "Fail login")

    context={
        'form':form,

    }

    return render(request,'registration/login.html',context)

def logout_req(request: HttpRequest):
    logout(request)
    return redirect('home')


def register_req(request: HttpRequest):
    form= KorisnikCreateForm(data=request.POST or None)
    if form.is_valid():
        user=form.save()
        login(request,user)
        return redirect('home')
    context={
        'form':form,

    }
    return render(request,'registration/register.html',context)
