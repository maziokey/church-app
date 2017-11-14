from django.conf.urls import url

from ..views import priest_list, priest_detail, PriestCreate, PriestUpdate, PriestDelete

urlpatterns = [
    url(r'^$', priest_list, name='churchadmin_priest_list'),
    url(r'^(?P<slug>[\w\-]+)/$', priest_detail, name='churchadmin_priest_detail'),
    url(r'^create/$', PriestCreate.as_view(), name='churchadmin_priest_create'),
    url(r'^(?P<slug>[\w\-]+)/update/$', PriestUpdate.as_view(), name='churchadmin_priest_update'),
    url(r'^(?P<slug>[\w\-]+)/delete/$', PriestDelete.as_view(), name='churchadmin_priest_delete'),
]
