from django.conf.urls import url

from ..views import parishioner_list, parishioner_detail

urlpatterns = [
    url(r'^$', parishioner_list, name='people_parishioner_list'),
    url(r'^(?P<slug>[\w\-]+)/$', parishioner_detail, name='people_parishioner_detail'),
]
