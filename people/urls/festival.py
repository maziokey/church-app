from django.conf.urls import url

from ..views import festival_list, festival_detail

urlpatterns = [
    url(r'^$', festival_list, name='people_festival_list'),
    url(r'^(?P<slug>[\w\-]+)/$', festival_detail, name='people_festival_detail'),
]
