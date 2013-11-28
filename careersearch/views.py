# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from careersearch.models import Post, News

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