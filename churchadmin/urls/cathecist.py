from django.conf.urls import url

from ..views import cathecist_list, cathecist_detail, CathecistCreate, CathecistUpdate, CathecistDelete

urlpatterns = [
    url(r'^$', cathecist_list, name='churchadmin_cathecist_list'),
    url(r'^create/$', CathecistCreate.as_view(), name='churchadmin_cathecist_create'),
    url(r'^(?P<slug>[\w\-]+)/$', cathecist_detail, name='churchadmin_cathecist_detail'),
    url(r'^(?P<slug>[\w\-]+)/delete/$', CathecistDelete.as_view(), name='churchadmin_cathecist_delete'),
    url(r'^(?P<slug>[\w\-]+)/update/$', CathecistUpdate.as_view(), name='churchadmin_cathecist_update'),
]
