from django.conf.urls import url

from ..views import sermon_list, sermon_detail, SermonCreate, SermonUpdate, SermonDelete

urlpatterns = [
    url(r'^$', sermon_list, name='blog_sermon_list'),
    url(r'^create/$', SermonCreate.as_view(), name='blog_sermon_create'),
    url(r'^(?P<year>\d{4})/'r'(?P<month>\d{1,2})/'r'(?P<slug>[\w\-]+)/$', sermon_detail, name='blog_sermon_detail'),
    url(r'^(?P<year>\d{4})/'r'(?P<month>\d{1,2})/'r'(?P<slug>[\w\-]+)/'r'delete/$', SermonDelete.as_view(), name='blog_sermon_delete'),
    url(r'^(?P<year>\d{4})/'r'(?P<month>\d{1,2})/'r'(?P<slug>[\w\-]+)/'r'update/$', SermonUpdate.as_view(), name='blog_sermon_update'),
]
