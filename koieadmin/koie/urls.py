from django.conf.urls import patterns, url

from koie import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^koie/(?P<koie_id>\d+)/$', views.koie_detail, name='koie_detail'),
)
