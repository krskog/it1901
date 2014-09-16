from django.conf.urls import patterns, url

from report import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<report_id>\d+)/$', views.detail, name='detail'),
)
