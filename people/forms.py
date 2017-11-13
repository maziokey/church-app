from django import forms
from django.core.exceptions import ValidationError

from .models import Society, Community, Sacrament, Festival, Parishioner

class SlugCleanMixin:
    """Mixin class for slug cleaning method."""

    def clean_slug(self):
        new_slug = (self.cleaned_data['slug'].lower())
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create".')
        return new_slug

class SocietyForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        Model = Society
        fields = '__all__'

class CommunityForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        Model = Community
        fields = '__all__'

class SacramentForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        Model = Sacrament
        fields = '__all__'

class FestivalForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        Model = Festival
        fields = '__all__'

class ParishionerForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        Model = Parishioner
        fields = '__all__'
