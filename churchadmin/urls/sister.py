from django.conf.urls import url

from ..views import sister_list, sister_detail, SisterCreate, SisterUpdate, SisterDelete

urlpatterns = [
    url(r'^$', sister_list, name='churchadmin_sister_list'),
    url(r'^(?P<slug>[\w\-]+)/$', sister_detail, name='churchadmin_sister_detail'),
    url(r'^create/$', SisterCreate.as_view(), name='churchadmin_sister_create'),
    url(r'^(?P<slug>[\w\-]+)/update/$', SisterUpdate.as_view(), name='churchadmin_sister_update'),
    url(r'^(?P<slug>[\w\-]+)/delete/$', SisterDelete.as_view(), name='churchadmin_sister_delete'),
]
