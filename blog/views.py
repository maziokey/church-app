from django.shortcuts import get_object_or_404, render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
from .utils import ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin

from .models import Sermon, Issue, Announcement, Project
from .forms import SermonForm, IssueForm, AnnouncementForm, ProjectForm

# Create your views here.
def sermon_list(request):
    return render(request, 'blog/sermon_list.html', {'sermon_list': Sermon.objects.all()})

def sermon_detail(request, year, month, slug):
    sermon = get_object_or_404(Sermon, pub_date__year=year, pub_date__month=month, slug=slug)
    return render(request, 'blog/sermon_detail.html', {'sermon': sermon})

def issue_list(request):
    return render(request, 'blog/issue_list.html', {'issue_list': Issue.objects.all()})

def issue_detail(request, year, month, slug):
    issue = get_object_or_404(Issue, pub_date__year=year, pub_date__month=month, slug=slug)
    return render(request, 'blog/issue_detail.html', {'issue': issue})

def announcement_list(request):
    return render(request, 'blog/announcement_list.html', {'announcement_list': Announcement.objects.all()})

def announcement_detail(request, year, month, slug):
    announcement = get_object_or_404(Announcement, pub_date__year=year, pub_date__month=month, slug=slug)
    return render(request, 'blog/announcement_detail.html', {'announcement': announcement})

def project_list(request):
    return render(request, 'blog/project_list.html', {'project_list': Project.objects.all()})

def project_detail(request, year, month, slug):
    project = get_object_or_404(Project, start_date__year=year, start_date__month=month, slug=slug)
    return render(request, 'blog/project_detail.html', {'project': project})

class SermonCreate(ObjectCreateMixin, View):
    form_class = SermonForm
    template_name = 'blog/sermon_form.html'

class IssueCreate(ObjectCreateMixin, View):
    form_class = IssueForm
    template_name = 'blog/issue_form.html'

class AnnouncementCreate(ObjectCreateMixin, View):
    form_class = AnnouncementForm
    template_name = 'blog/announcement_form.html'

class ProjectCreate(ObjectCreateMixin, View):
    form_class = ProjectForm
    template_name = 'blog/project_form.html'

class SermonUpdate(ObjectUpdateMixin, View):
    form_class = SermonForm
    model = Sermon
    template_name = ('blog/sermon_form_update.html')

class IssueUpdate(ObjectUpdateMixin, View):
    form_class = IssueForm
    model = Issue
    template_name = ('blog/issue_form_update.html')

class AnnouncementUpdate(ObjectUpdateMixin, View):
    form_class = AnnouncementForm
    model = Announcement
    template_name = ('blog/announcement_form_update.html')

class ProjectUpdate(View):
    form_class = ProjectForm
    model = Project
    template_name = 'blog/project_form_update.html'

    def get_object(self, year, month, slug):
        return get_object_or_404(self.model, start_date__year=year, start_date__month=month, slug=slug)

    def get(self, request, year, month, slug):
        post = self.get_object(year, month, slug)
        context = {'form': self.form_class(instance=post), 'post': post, }
        return render(request, self.template_name, context)

    def post(self, request, year, month, slug):
        post = self.get_object(year, month, slug)
        bound_form = self.form_class(request.POST, instance=post)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        else:
            context = {'form': bound_form, 'post': post, }
            return render(request, self.template_name, context)

class SermonDelete(ObjectDeleteMixin, View):
    model = Sermon
    success_url = reverse_lazy('blog_sermon_list')
    template_name = ('blog/sermon_confirm_delete.html')

class IssueDelete(ObjectDeleteMixin, View):
    model = Issue
    success_url = reverse_lazy('blog_issue_list')
    template_name = ('blog/issue_confirm_delete.html')

class AnnouncementDelete(ObjectDeleteMixin, View):
    model = Announcement
    success_url = reverse_lazy('blog_announcement_list')
    template_name = ('blog/announcement_confirm_delete.html')

class ProjectDelete(View):

    def get(self, request, year, month, slug):
        post = get_object_or_404(Project, start_date__year=year, start_date__month=month, slug__iexact=slug)
        return render(request, 'blog/project_confirm_delete.html', {'post': post})

    def post(self, request, year, month, slug):
        post = get_object_or_404(Project, start_date__year=year, start_date__month=month, slug__iexact=slug)
        post.delete()
        return redirect('blog_project_list')
