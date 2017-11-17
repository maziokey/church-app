from django import forms
from django.core.exceptions import ValidationError

from .models import Sermon, Issue, Announcement, Project

class SlugCleanMixin:
    """Mixin class for slug cleaning method."""

    def clean_slug(self):
        new_slug = (self.cleaned_data['slug'].lower())
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create".')
        return new_slug

class SermonForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Sermon
        fields = '__all__'

class IssueForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Issue
        fields = '__all__'

class AnnouncementForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Announcement
        fields = '__all__'

class ProjectForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
