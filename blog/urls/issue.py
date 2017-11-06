from django.conf.urls import url

from ..views import issue_list, issue_detail

urlpatterns = [
    url(r'^$', issue_list, name='blog_issue_list'),
    url(r'^(?P<year>\d{4})/'r'(?P<month>\d{1,2})/'r'(?P<slug>[\w\-]+)/$', issue_detail, name='blog_issue_detail'),
]
