from django.conf.urls import url

from ..views import alterboy_list, alterboy_detail, AlterBoyCreate, AlterBoyUpdate, AlterBoyDelete

urlpatterns = [
    url(r'^$', alterboy_list, name='churchadmin_alterboy_list'),
    url(r'^(?P<slug>[\w\-]+)/$', alterboy_detail, name='churchadmin_alterboy_detail'),
    url(r'^create/$', AlterBoyCreate.as_view(), name='churchadmin_alterboy_create'),
    url(r'^(?P<slug>[\w\-]+)/update/$', AlterBoyUpdate.as_view(), name='churchadmin_alterboy_update'),
    url(r'^(?P<slug>[\w\-]+)/delete/$', AlterBoyDelete.as_view(), name='churchadmin_alterboy_delete'),
]
