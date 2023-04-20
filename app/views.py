from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q

from .models import Szakdoga
from .forms import SzakdogaForm

def index(request):
    form = SzakdogaForm(request.POST or None)
    if(request.method == 'POST'):
        if(form.is_valid()):
                form.save()
                form = SzakdogaForm()
    else:
        form = SzakdogaForm()

    szakdolgozatok = Szakdoga.objects.all()

    context = {
        'form': form,
        'szakdolgozatok': szakdolgozatok
    }

    return render(request, 'app/index.html', context = context)

def szakdogaModositas(request, id):
    szakdoga = get_object_or_404(Szakdoga, pk = id)

    form = SzakdogaForm(request.POST or None, instance = szakdoga)
    if(request.method == 'POST'):
        if(form.is_valid()):
            form.save()
            return redirect(index)
        
    context = {
        'form': form
    }

    return render(request, 'app/modositas.html', context = context)

def szakdogaTorlese(request, id):
    szakdoga = get_object_or_404(Szakdoga, pk = id)
    szakdoga.delete()
    return redirect(index)