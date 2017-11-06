from django.conf.urls import url

from ..views import sacrament_list, sacrament_detail

urlpatterns = [
    url(r'^$', sacrament_list, name='people_sacrament_list'),
    url(r'^(?P<slug>[\w\-]+)/$', sacrament_detail, name='people_sacrament_detail'),
]
