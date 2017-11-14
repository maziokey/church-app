from django.shortcuts import get_object_or_404, render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
from .utils import ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin

from .models import Society, Community, Sacrament, Festival, Parishioner
from .forms import SocietyForm, CommunityForm, SacramentForm, FestivalForm, ParishionerForm

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

class SocietyCreate(ObjectCreateMixin, View):
    form_class = SocietyForm
    template_name = 'people/society_form.html'

class CommunityCreate(ObjectCreateMixin, View):
    form_class = CommunityForm
    template_name = 'people/community_form.html'

class FestivalCreate(ObjectCreateMixin, View):
    form_class = FestivalForm
    template_name = 'people/festival_form.html'

class ParishionerCreate(ObjectCreateMixin, View):
    form_class = ParishionerForm
    template_name = 'people/parishioner_form.html'

class SocietyUpdate(ObjectUpdateMixin, View):
    form_class = SocietyForm
    model = Society
    template_name = ('people/society_form_update.html')

class CommunityUpdate(ObjectUpdateMixin, View):
    form_class = CommunityForm
    model = Community
    template_name = ('people/community_form_update.html')

class FestivalUpdate(ObjectUpdateMixin, View):
    form_class = FestivalForm
    model = Festival
    template_name = ('people/festival_form_update.html')

class ParishionerUpdate(ObjectUpdateMixin, View):
    form_class = ParishionerForm
    model = Parishioner
    template_name = ('people/parishioner_form_update.html')

class SocietyDelete(ObjectDeleteMixin, View):
    model = Society
    success_url = reverse_lazy('people_society_list')
    template_name = ('people/society_confirm_delete.html')

class CommunityDelete(ObjectDeleteMixin, View):
    model = Community
    success_url = reverse_lazy('people_community_list')
    template_name = ('people/community_confirm_delete.html')

class FestivalDelete(ObjectDeleteMixin, View):
    model = Festival
    success_url = reverse_lazy('people_festival_list')
    template_name = ('people/festival_confirm_delete.html')

class ParishionerDelete(ObjectDeleteMixin, View):
    model = Parishioner
    success_url = reverse_lazy('people_parishioner_list')
    template_name = ('people/parishioner_confirm_delete.html')
