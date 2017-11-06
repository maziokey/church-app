from django.conf.urls import url

from ..views import announcement_list, announcement_detail

urlpatterns = [
    url(r'^$', announcement_list, name='blog_announcement_list'),
    url(r'^(?P<year>\d{4})/'r'(?P<month>\d{1,2})/'r'(?P<slug>[\w\-]+)/$', announcement_detail, name='blog_announcement_detail'),
]
