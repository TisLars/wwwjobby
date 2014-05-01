from django.conf.urls import patterns, include, url
from careersearch.models import Post, News
from careersearch import views

urlpatterns = patterns('',

	# Url leads to main page
	# jobby.nl/
	url(r'^$', 'careersearch.views.index'),

	# Url leads to a detail page for a vacancy
	# e.g: jobby.nl/careersearch/2
	# page to vacancy id=2
	url(r'^(?P<id>\d+)$', 'careersearch.views.vacancyDetail'),

	# Url leads to a detail page for a news
	# e.g: jobby.nl/news/2
	# page to news id=2
	url(r'^news/(?P<id>\d+)$', 'careersearch.views.newsDetail'),

	# Url leads to an info page
	url(r'info/$', 'careersearch.views.info'),

	# Url leads to a contact page
	url(r'contact/$', 'careersearch.views.contact'),

	#User auth
	url(r'^accounts/login/$', 'careersearch.views.login'),
	url(r'^accounts/auth', 'careersearch.views.auth_view'),
	url(r'^accounts/logout/$', 'careersearch.views.logout'),
	url(r'^accounts/invalid/$', 'careersearch.views.invalid_login'),
)