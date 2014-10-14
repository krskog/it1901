from django.conf.urls import patterns, url

from reservation import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<reservation_id>\d+)/$', views.detail, name='detail'),
)
