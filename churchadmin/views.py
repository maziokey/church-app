from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View
from .utils import ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin

from .models import Priest, Sister, Cathecist, AlterBoy
from .forms import PriestForm, SisterForm, CathecistForm, AlterBoyForm

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

class PriestCreate(ObjectCreateMixin, View):
    form_class = PriestForm
    template_name = 'churchadmin/priest_form.html'

class SisterCreate(ObjectCreateMixin, View):
    form_class = SisterForm
    template_name = 'churchadmin/sister_form.html'

class CathecistCreate(ObjectCreateMixin, View):
    form_class = CathecistForm
    template_name = 'churchadmin/cathecist_form.html'

class AlterBoyCreate(ObjectCreateMixin, View):
    form_class = AlterBoyForm
    template_name = 'churchadmin/alterboy_form.html'

class PriestUpdate(ObjectUpdateMixin, View):
    form_class = PriestForm
    model = Priest
    template_name = ('churchadmin/priest_form_update.html')

class SisterUpdate(ObjectUpdateMixin, View):
    form_class = SisterForm
    model = Sister
    template_name = ('churchadmin/sister_form_update.html')

class CathecistUpdate(ObjectUpdateMixin, View):
    form_class = CathecistForm
    model = Cathecist
    template_name = ('churchadmin/cathecist_form_update.html')

class AlterBoyUpdate(ObjectUpdateMixin, View):
    form_class = AlterBoyForm
    model = AlterBoy
    template_name = ('churchadmin/alterboy_form_update.html')

class PriestDelete(ObjectDeleteMixin, View):
    model = Priest
    success_url = reverse_lazy('churchadmin_priest_list')
    template_name = ('churchadmin/priest_confirm_delete.html')

class SisterDelete(ObjectDeleteMixin, View):
    model = Sister
    success_url = reverse_lazy('churchadmin_sister_list')
    template_name = ('churchadmin/sister_confirm_delete.html')

class CathecistDelete(ObjectDeleteMixin, View):
    model = Cathecist
    success_url = reverse_lazy('churchadmin_cathecist_list')
    template_name = ('churchadmin/cathecist_confirm_delete.html')

class AlterBoyDelete(ObjectDeleteMixin, View):
    model = AlterBoy
    success_url = reverse_lazy('churchadmin_alterboy_list')
    template_name = ('churchadmin/alterboy_confirm_delete.html')
