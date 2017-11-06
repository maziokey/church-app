from django.conf.urls import url

from ..views import cathecist_list, cathecist_detail

urlpatterns = [
    url(r'^$', cathecist_list, name='churchadmin_cathecist_list'),
    url(r'^(?P<slug>[\w\-]+)/$', cathecist_detail, name='churchadmin_cathecist_detail'),
]
