from django.conf.urls import url

from ..views import festival_list, festival_detail, FestivalCreate, FestivalUpdate, FestivalDelete

urlpatterns = [
    url(r'^$', festival_list, name='people_festival_list'),
    url(r'^create/$', FestivalCreate.as_view(), name='people_festival_create'),
    url(r'^(?P<slug>[\w\-]+)/$', festival_detail, name='people_festival_detail'),
    url(r'^(?P<slug>[\w\-]+)/delete/$', FestivalDelete.as_view(), name='people_festival_delete'),
    url(r'^(?P<slug>[\w\-]+)/update/$', FestivalUpdate.as_view(), name='people_festival_update'),
]
