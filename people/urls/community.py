from django.conf.urls import url

from ..views import community_list, community_detail, CommunityCreate, CommunityUpdate, CommunityDelete

urlpatterns = [
    url(r'^$', community_list, name='people_community_list'),
    url(r'^create/$', CommunityCreate.as_view(), name='people_community_create'),
    url(r'^(?P<slug>[\w\-]+)/$', community_detail, name='people_community_detail'),
    url(r'^(?P<slug>[\w\-]+)/delete/$', CommunityDelete.as_view(), name='people_community_delete'),
    url(r'^(?P<slug>[\w\-]+)/update/$', CommunityUpdate.as_view(), name='people_community_update'),
]
