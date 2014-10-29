from django.conf.urls import patterns, url

from koie import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^koier/$', views.koie_index, name='koie_index'),
    url(r'^koie/(?P<koie_id>\d+)/$', views.koie_detail, name='koie_detail'),
    url(r'^reservation/$', views.reserve_koie, name='reserve_koie'),
    url(r'^reservation/(?P<koie_id>\d+)/$', views.reserve_koie, name='reserve_koie'),
    url(r'^reservation/upcoming/$', views.next_reservations, name='next_reservations'),
    url(r'^report/latest/(?P<slug>[^\.]+)', views.latest_reports, name='latest_reports'),
    url(r'^report/latest', views.latest_reports, name='latest_reports'),
    url(r'^report/(?P<report_id>\d+)/$', views.report_koie, name='report_koie'),
    url(r'^report/(?P<report_id>\d+)/read/$', views.read_report, name='read_report'),
)
