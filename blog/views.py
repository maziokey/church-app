from django.shortcuts import get_object_or_404, render, redirect
from .models import Sermon, Issue, Announcement, Project

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
