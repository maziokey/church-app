from django.conf.urls import url

from ..views import project_list, project_detail

urlpatterns = [
    url(r'^$', project_list, name='blog_project_list'),
    url(r'^(?P<year>\d{4})/'r'(?P<month>\d{1,2})/'r'(?P<slug>[\w\-]+)/$', project_detail, name='blog_project_detail'),
]
