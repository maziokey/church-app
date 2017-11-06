from django.conf.urls import url

from ..views import society_list, society_detail

urlpatterns = [
    url(r'^$', society_list, name='people_society_list'),
    url(r'^(?P<slug>[\w\-]+)/$', society_detail, name='people_society_detail'),
]
