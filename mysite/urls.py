"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from collection import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', views.home, name='home'),
	url(r'^climbs/(?P<slug>[-\w]+)/$', views.climb_detail, name='climb_detail'),
	url(r'^climbs/condensed/(?P<slug>[-\w]+)/$', views.climb_detail_condensed, name='climb_detail_condensed'),
	url(r'^climb_list/$', views.climb_list, name='climb_list'),
	url(r'^new_climb/$', views.new_climb, name='new_climb'),
	url(r'^log_climb/$', views.log_climb, name='log_climb'),
	url(r'^add_video/$', views.add_video, name='add_video'),
	url(r'^user_list/$', views.user_list, name='user_list'),
	url(r'^users/(?P<uid>\d+)/$', views.user_profile, name='user_profile'),
]
