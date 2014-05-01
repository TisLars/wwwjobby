from django.conf.urls import patterns, include, url
from careersearch.models import Post, News
from careersearch import views

urlpatterns = patterns('',

	# Url leads to a detail page for a news
	# e.g: jobby.nl/news/2
	# page to news id=2
	url(r'^news/(?P<id>\d+)$', 'careersearch.views.newsDetail'),

	# Url leads to an info page
	url(r'info/$', 'careersearch.views.info'),

	# Url leads to a contact page
	url(r'contact/$', 'careersearch.views.contact'),

	#Url leads to search page
	url(r'^search/', 'careersearch.views.search_vacancies'),
)