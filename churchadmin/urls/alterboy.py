from django.conf.urls import url

from ..views import alterboy_list, alterboy_detail

urlpatterns = [
    url(r'^$', alterboy_list, name='churchadmin_alterboy_list'),
    url(r'^(?P<slug>[\w\-]+)/$', alterboy_detail, name='churchadmin_alterboy_detail'),
]
