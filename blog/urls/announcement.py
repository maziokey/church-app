from django.conf.urls import url

from ..views import announcement_list, announcement_detail, AnnouncementCreate, AnnouncementUpdate, AnnouncementDelete

urlpatterns = [
    url(r'^$', announcement_list, name='blog_announcement_list'),
    url(r'^(?P<year>\d{4})/'r'(?P<month>\d{1,2})/'r'(?P<slug>[\w\-]+)/$', announcement_detail, name='blog_announcement_detail'),
    url(r'^create/$', AnnouncementCreate.as_view(), name='blog_announcement_create'),
    url(r'^(?P<year>\d{4})/'r'(?P<month>\d{1,2})/'r'(?P<slug>[\w\-]+)/'r'update/$', AnnouncementUpdate.as_view(), name='blog_announcement_update'),
    url(r'^(?P<year>\d{4})/'r'(?P<month>\d{1,2})/'r'(?P<slug>[\w\-]+)/'r'delete/$', AnnouncementDelete.as_view(), name='blog_announcement_delete'),
]
