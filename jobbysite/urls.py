from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jobbysite.views.home', name='home'),
    # url(r'^jobbysite/', include('jobbysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^', include('careersearch.urls')),
    url(r'^', include('userprofile.urls')),
    url(r'^careersearch/', include('careersearch.urls')),
    url(r'^dashboards/', include('dashboards.urls')),

	# User auth
	url(r'^accounts/login/$', 'userprofile.views.login'),
	url(r'^accounts/auth/$', 'userprofile.views.auth_view'),
	url(r'^accounts/logout/$', 'userprofile.views.logout'),
	url(r'^accounts/loggedin/$', 'userprofile.views.loggedin'),
	url(r'^accounts/invalid/$', 'userprofile.views.invalid_login'),
    url(r'^accounts/register/$', 'userprofile.views.register_user'),
    url(r'^accounts/register_success/$', 'userprofile.views.register_success'),
    url(r'^accounts/edit_profile/$', 'userprofile.views.edit_profile'),
)
