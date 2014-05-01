from django.conf.urls import patterns, url

from userprofile import views

urlpatterns = patterns('',
    
    # Url leads to main page
    # jobby.nl/
    url(r'^$', views.index, name='index'),
    
    url(r'^vacancy/overview/$', views.index, name='index'),
    url(r'^vacancy/(?P<id>\d+)$', views.vacancydetail, name='vacancyDetail'),
    
    url(r'^cv/overview/$', views.cvoverview, name='cvoverview'),
    
    url(r'^cv/(?P<cv_id>\d+)/$', views.cvdetail, name='cvdetail')
)