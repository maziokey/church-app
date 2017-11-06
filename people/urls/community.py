from django.conf.urls import url

from ..views import community_list, community_detail

urlpatterns = [
    url(r'^$', community_list, name='people_community_list'),
    url(r'^(?P<slug>[\w\-]+)/$', community_detail, name='people_community_detail'),
]
