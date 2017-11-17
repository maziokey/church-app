from django.conf.urls import url

from ..views import society_list, society_detail, SocietyCreate, SocietyUpdate, SocietyDelete

urlpatterns = [
    url(r'^$', society_list, name='people_society_list'),
    url(r'^create/$', SocietyCreate.as_view(), name='people_society_create'),
    url(r'^(?P<slug>[\w\-]+)/$', society_detail, name='people_society_detail'),
    url(r'^(?P<slug>[\w\-]+)/delete/$', SocietyDelete.as_view(), name='people_society_delete'),
    url(r'^(?P<slug>[\w\-]+)/update/$', SocietyUpdate.as_view(), name='people_society_update'),
]
