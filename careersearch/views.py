# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import Context, loader
from django.shortcuts import render, render_to_response
from careersearch.models import Post, News
from careersearch.forms import ContactForm

# View to display ALL news items and ALL vacancy items
def index(request):
	news_list = News.objects.order_by('-date')[:6]
	vacancy_list = Post.objects.order_by('-date')[:10]
	t = loader.get_template('vacancy.html')
	c = Context({
		'news_list': news_list,
		'vacancy_list': vacancy_list,})
	return HttpResponse(t.render(c))

# View to display ALL news items and 1 detailed vacancy item
def vacancyDetail(request, id):
	news_list = News.objects.order_by('-date')[:6]
	detail_vacancy_list = Post.objects.get(id=id)
	t = loader.get_template('vacancydetail.html')
	c = Context({
		'news_list': news_list,
		'detail_vacancy_list': detail_vacancy_list,})
	return HttpResponse(t.render(c))

# View to display ALL news items and 1 detailed news item
def newsDetail(request, id):
	news_list = News.objects.order_by('-date')[:6]
	detail_news_list = News.objects.get(id=id)
	t = loader.get_template('news.html')
	c = Context({
		'news_list': news_list,
		'detail_news_list': detail_news_list,})
	return HttpResponse(t.render(c))

# View to display ALL news items and info item
def info(request):
	news_list = News.objects.order_by('-date')[:6]
	t = loader.get_template('info.html')
	c = Context({
		'news_list': news_list,})
	return HttpResponse(t.render(c))

# View to display ALL news items and contact form
def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']
			cc_myself = form.cleaned_data['cc_myself']

			recipients = ['lhoevenaar@hushmail.com']
			if cc_myself:
				recipients.append(sender)

			from django.core.mail import send_mail
			send_mail(subject, message, sender, recipients)

			return HttpResponse('Bedankt voor uw bericht, deze zal binnen 3 werkdagen beantwoord worden.')

	else:
		form = ContactForm()

	return render(request, 'contact.html', {
		'form': form,
	})

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
	return render_to_response('loggedin.html',
		{'full_name': request.username})

def invalid_login(request):
	return render_to_response('invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')