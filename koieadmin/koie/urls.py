from django.conf.urls import patterns, url

from koie import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^koier/$', views.koie_index, name='koie_index'),
    url(r'^koie/(?P<koie_id>\d+)/$', views.koie_detail, name='koie_detail'),
    url(r'^reserve/$', views.reserve_koie, name='reserve_koie'),
)
