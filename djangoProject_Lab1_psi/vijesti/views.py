from django.shortcuts import render

from django.http import HttpResponse
from .models import *
from django.template import loader
from django.shortcuts import render
# Create your views here.
def index(request):

    vijesti=Vest.objects.all()
    response="<br><hr>".join([str(v) for v in vijesti])
    #template=loader.get_template('vijesti/index.html')
    context={
        'vijesti':vijesti
    }
    # return HttpResponse(template.render(context,request))
    return render(request,'vijesti/index.html',context)

from django.http import Http404
from .formicas import VestForm
def vijest(request,vijest_id):
    try:
        vijest= Vest.objects.get(pk=vijest_id)
        komenatri=Komentar.objects.filter(vest=vijest_id)

        form = VestForm()

        if(request.method=='POST'):
            form=VestForm(request.POST)

            if form.is_valid():
                autor=form.cleaned_data['autor']
                sadrzaj=form.cleaned_data['sadrzaj']
                autorobj=Autor.objects.get(korime=autor)
                novkom=Komentar(autor=autorobj,sadrzaj=sadrzaj,vest=vijest)
                novkom.save()
        context = {
            'vijest': vijest,
            'komentari': komenatri,
            'form': form
        }
        return render(request, 'vijesti/vijest.html', context)
    except Vest.DoesNotExist:
        raise Http404("Vijest nije pronadjena")




