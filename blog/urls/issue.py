from django.conf.urls import url

from ..views import issue_list, issue_detail, IssueCreate, IssueUpdate, IssueDelete

urlpatterns = [
    url(r'^$', issue_list, name='blog_issue_list'),
    url(r'^create/$', IssueCreate.as_view(), name='blog_issue_create'),
    url(r'^(?P<year>\d{4})/'r'(?P<month>\d{1,2})/'r'(?P<slug>[\w\-]+)/$', issue_detail, name='blog_issue_detail'),
    url(r'^(?P<year>\d{4})/'r'(?P<month>\d{1,2})/'r'(?P<slug>[\w\-]+)/'r'delete/$', IssueDelete.as_view(), name='blog_issue_delete'),
    url(r'^(?P<year>\d{4})/'r'(?P<month>\d{1,2})/'r'(?P<slug>[\w\-]+)/'r'update/$', IssueUpdate.as_view(), name='blog_issue_update'),
]
