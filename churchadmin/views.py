from django.shortcuts import get_object_or_404, render, redirect
from .models import Priest, Sister, Cathecist, AlterBoy

# Create your views here.
def priest_list(request):
    return render(request, 'churchadmin/priest_list.html', {'priest_list': Priest.objects.all()})

def priest_detail(request, slug):
    priest = get_object_or_404(Priest, slug__iexact=slug)
    return render(request, 'churchadmin/priest_detail.html', {'priest': priest})

def sister_list(request):
    return render(request, 'churchadmin/sister_list.html', {'sister_list': Sister.objects.all()})

def sister_detail(request, slug):
    sister = get_object_or_404(Sister, slug__iexact=slug)
    return render(request, 'churchadmin/sister_detail.html', {'sister': sister})

def cathecist_list(request):
    return render(request, 'churchadmin/cathecist_list.html', {'cathecist_list': Cathecist.objects.all()})

def cathecist_detail(request, slug):
    cathecist = get_object_or_404(Cathecist, slug__iexact=slug)
    return render(request, 'churchadmin/cathecist_detail.html', {'cathecist': cathecist})

def alterboy_list(request):
    return render(request, 'churchadmin/alterboy_list.html', {'alterboy_list': AlterBoy.objects.all()})

def alterboy_detail(request, slug):
    alterboy = get_object_or_404(AlterBoy, slug__iexact=slug)
    return render(request, 'churchadmin/alterboy_detail.html', {'alterboy': alterboy})
