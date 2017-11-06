from django.conf.urls import url

from ..views import sister_list, sister_detail

urlpatterns = [
    url(r'^$', sister_list, name='churchadmin_sister_list'),
    url(r'^(?P<slug>[\w\-]+)/$', sister_detail, name='churchadmin_sister_detail'),
]
