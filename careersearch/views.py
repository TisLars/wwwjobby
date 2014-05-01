# Create your views here.
from django.core.context_processors import csrf
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, RequestContext
from careersearch.models import News
from careersearch.forms import ContactForm
from userprofile.models import Vacancy

from haystack.query import SearchQuerySet
from haystack.views import SearchView
from haystack.views import search_view_factory
from haystack.forms import HighlightedSearchForm

# View to display ALL news items and 1 detailed news item
def newsDetail(request, id):
	news_list = News.objects.order_by('-date')[:6]
	detail_news_list = News.objects.get(id=id)
	c = Context({
		'news_list': news_list,
		'detail_news_list': detail_news_list,})
	return render(request, 'careersearch/news.html', c, context_instance=RequestContext(request))

# View to display ALL news items and info item
def info(request):
	news_list = News.objects.order_by('-date')[:6]
	c = Context({
		'news_list': news_list,})
	return render(request, 'careersearch/info.html', c, context_instance=RequestContext(request))

# View to display ALL news items and contact form
def contact(request):
	news_list = News.objects.order_by('-date')[:6]
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():			
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']
			recipients = ['lhoevenaar@hushmail.com']
			
			send_mail(subject, message, sender, recipients)

			return HttpResponse('Bericht succesvol verzonden.')

	else:
		form = ContactForm()

	c = RequestContext(request, { 
		'form': form,	
		'news_list': news_list,
	})
	
	return render(request, 'careersearch/contact.html', c, context_instance=RequestContext(request))

def search_vacancies(request):
	post_type = str(request.GET.get('q')).lower()
	sqs = SearchQuerySet().all()
	view = search_view_factory(
		view_class=SearchView,
		template='search/search.html',
		searchqueryset=sqs,
		form_class=HighlightedSearchForm
		)
	return view(request)