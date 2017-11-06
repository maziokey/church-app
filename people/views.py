from django.shortcuts import get_object_or_404, render, redirect
from .models import Society, Community, Sacrament, Festival, Parishioner

# Create your views here.
def society_list(request):
    return render(request, 'people/society_list.html', {'society_list': Society.objects.all()})

def society_detail(request, slug):
    society = get_object_or_404(Society, slug__iexact=slug)
    return render(request, 'people/society_detail.html', {'society': society})

def community_list(request):
    return render(request, 'people/community_list.html', {'community_list': Community.objects.all()})

def community_detail(request, slug):
    community = get_object_or_404(Community, slug__iexact=slug)
    return render(request, 'people/community_detail.html', {'community': community})

def sacrament_list(request):
    return render(request, 'people/sacrament_list.html', {'sacrament_list': Sacrament.objects.all()})

def sacrament_detail(request, slug):
    sacrament = get_object_or_404(Sacrament, slug__iexact=slug)
    return render(request, 'people/sacrament_detail.html', {'sacrament': sacrament})

def festival_list(request):
    return render(request, 'people/festival_list.html', {'festival_list': Festival.objects.all()})

def festival_detail(request, slug):
    festival = get_object_or_404(Festival, slug__iexact=slug)
    return render(request, 'people/festival_detail.html', {'festival': festival})

def parishioner_list(request):
    return render(request, 'people/parishioner_list.html', {'parishioner_list': Parishioner.objects.all()})

def parishioner_detail(request, slug):
    parishioner = get_object_or_404(Parishioner, slug__iexact=slug)
    return render(request, 'people/parishioner_detail.html', {'parishioner': parishioner})
