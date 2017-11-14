from django.conf.urls import url

from ..views import parishioner_list, parishioner_detail, ParishionerCreate, ParishionerUpdate, ParishionerDelete

urlpatterns = [
    url(r'^$', parishioner_list, name='people_parishioner_list'),
    url(r'^(?P<slug>[\w\-]+)/$', parishioner_detail, name='people_parishioner_detail'),
    url(r'^create/$', ParishionerCreate.as_view(), name='people_parishioner_create'),
    url(r'^(?P<slug>[\w\-]+)/update/$', ParishionerUpdate.as_view(), name='people_parishioner_update'),
    url(r'^(?P<slug>[\w\-]+)/delete/$', ParishionerDelete.as_view(), name='people_parishioner_delete'),
]
