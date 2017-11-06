from django.conf.urls import url

from ..views import sermon_list, sermon_detail

urlpatterns = [
    url(r'^$', sermon_list, name='blog_sermon_list'),
    url(r'^(?P<year>\d{4})/'r'(?P<month>\d{1,2})/'r'(?P<slug>[\w\-]+)/$', sermon_detail, name='blog_sermon_detail'),
]
