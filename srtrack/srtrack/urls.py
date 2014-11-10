from django.conf.urls import patterns, include, url
from django.contrib import admin

from srmap import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^tracker/$', views.tracker, name='tracker'),
    # url(r'^srmap/', include('srmap.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
