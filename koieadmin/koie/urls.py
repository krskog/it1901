from django.conf.urls import patterns, url

from koie import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<koie_id>\d+)/$', views.detail, name='detail'),
)
