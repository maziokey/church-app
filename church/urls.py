"""church URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from blog.urls import sermon as sermon_urls, issue as issue_urls, announcement as announcement_urls, project as project_urls
from churchadmin.urls import priest as priest_urls, sister as sister_urls, cathecist as cathecist_urls, alterboy as alterboy_urls
from people.urls import society as society_urls, community as community_urls, sacrament as sacrament_urls, festival as festival_urls, parishioner as parishioner_urls
#from churchadmin.views import priest_list, priest_detail

urlpatterns = [
    url(r'^$', redirect_root),
    url(r'^admin/', admin.site.urls),
    url(r'^sermon/', include(sermon_urls)),
    url(r'^issue/', include(issue_urls)),
    url(r'^announcement/', include(announcement_urls)),
    url(r'^project/', include(project_urls)),
    url(r'^priest/', include(priest_urls)),
    url(r'^sister/', include(sister_urls)),
    url(r'^cathecist/', include(cathecist_urls)),
    url(r'^alterboy/', include(alterboy_urls)),
    url(r'^society/', include(society_urls)),
    url(r'^community/', include(community_urls)),
    url(r'^sacrament/', include(sacrament_urls)),
    url(r'^festival/', include(festival_urls)),
    url(r'^parishioner/', include(parishioner_urls)),
    #url(r'^priest/(?P<slug>[\w\-]+)/$', priest_detail, name='churchadmin_priest_detail'),
]
