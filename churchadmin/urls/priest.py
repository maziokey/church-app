from django.conf.urls import url

from ..views import priest_list, priest_detail

urlpatterns = [
    url(r'^$', priest_list, name='churchadmin_priest_list'),
    url(r'^(?P<slug>[\w\-]+)/$', priest_detail, name='churchadmin_priest_detail'),
]
