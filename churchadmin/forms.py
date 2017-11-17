from django import forms
from django.core.exceptions import ValidationError

from .models import Priest, Sister, Cathecist, AlterBoy

class SlugCleanMixin:
    """Mixin class for slug cleaning method."""

    def clean_slug(self):
        new_slug = (self.cleaned_data['slug'].lower())
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create".')
        return new_slug

class PriestForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Priest
        fields = '__all__'

class SisterForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Sister
        fields = '__all__'

class CathecistForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Cathecist
        fields = '__all__'

class AlterBoyForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = AlterBoy
        fields = '__all__'
