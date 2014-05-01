# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404, RequestContext, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.template import RequestContext, loader, Context

from userprofile.models import CV, Vacancy, Match
from userprofile.forms import UserProfileForm
from careersearch.models import Post, News
from django.db.models.query import QuerySet
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random


news_list = News.objects.order_by('-date')[:6]

# View to display ALL news items and the 10 last vacancy items
def index(request):
    vacancy_list = Vacancy.objects.exclude(job='null').order_by('-timestamp')
     
    paginator = Paginator(vacancy_list, 5)
    
    page = request.GET.get('page')
    try:
        vacancys = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        vacancys = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        vacancys = paginator.page(paginator.num_pages)
    
    context = Context({
        'news_list': news_list,
        'vacancy_list': vacancys,})
    
    return render(request, 'userprofile/vacancy.html', context, context_instance=RequestContext(request))

# View to display 6 news items and 1 detailed vacancy item
def vacancydetail(request, id):
    vacancy = get_object_or_404(Vacancy, id=id)

    try:
        match = Match.objects.filter(vacancy_id=id)
    except Match.DoesNotExist:
        match = None
    
    context = Context({
        'vacancy': vacancy,
        'news_list': news_list,
        'match' : match,
    })
    
    return render(request, 'userprofile/vacancydetail.html', context, context_instance=RequestContext(request))

def cvoverview(request):
    cvlist = CV.objects.order_by('-post_date')
    
    paginator = Paginator(cvlist, 20)
    
    page = request.GET.get('page')
    try:
        cvs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        cvs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        cvs = paginator.page(paginator.num_pages)
    
    context = RequestContext(request, {
       'cvlist': cvs,
       'news_list': news_list,
    })
    return render(request, 'userprofile/cvlist.html', context, context_instance=RequestContext(request))
    
def cvdetail(request, cv_id):
    cv = get_object_or_404(CV, pk=cv_id)
    
    try:
        match = Match.objects.filter(cv_id=cv_id).order_by('?')[:5]
    except Match.DoesNotExist:
        match = None
        
    context = RequestContext(request, {
       'cv': cv,
       'news_list': news_list,
       'match' : match,
    })
    return render(request, 'userprofile/cvdetail.html', context, context_instance=RequestContext(request))

# inlog view
def login(request):
    c = {}
    c.update(csrf(request))
    
    render_context = RequestContext(request, {
        'news_list': news_list,
        'c' : c,
    })
    
    return render_to_response('accounts/login.html', render_context, context_instance=RequestContext(request))

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

# succesvol ingelogd
@login_required
def loggedin(request):
    c = RequestContext(request, {
        'news_list': news_list,
        'full_name': request.user.username,
    })

    return render_to_response('accounts/loggedin.html', c, context_instance=RequestContext(request))

# verkeerde credentials
def invalid_login(request):
    c = RequestContext(request, {
        'news_list': news_list,
    })

    return render(request, 'accounts/invalid.html', c, context_instance=RequestContext(request))

# user is uitgelogd
def logout(request):
    auth.logout(request)

    c = RequestContext(request, {
        'news_list': news_list,
    })
    
    return render(request, 'accounts/logout.html', c, context_instance=RequestContext(request))

# registreer gebruiker view
def register_user(request):
    error = "";
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
        else:
            error = form.errors

    args = {}
    args.update(csrf(request))

    args['form'] = UserCreationForm()
    
    c = RequestContext(request, {
        'news_list' : news_list,
        'args' : args,
        'errors' : error,
    })

    return render_to_response('accounts/register.html', c, context_instance=RequestContext(request))

# registratie voltooid view
def register_success(request):
    c = RequestContext(request, {
        'news_list': news_list,
    })

    return render_to_response('accounts/register_success.html', c, context_instance=RequestContext(request))

# beheren van profiel view
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/loggedin')

    else:
        user = request.user
        profile = user.profile
        form = UserProfileForm(instance=profile)

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('accounts/edit_profile.html', args, context_instance=RequestContext(request))

@login_required
def usereditprofile_form(request):
    if request.method == 'GET':
        form = UserProfileCVForm()
    else:
        form = UserProfileCVForm(request.POST)

        if form.is_valid():
            user = form.cleaned_data['user']
            date_of_birth = form.cleaned_data['date_of_birth']
            skill = form.cleaned_data['skill']
            education = form.cleaned_data['education']
            city = form.cleaned_data['city']
            province = form.cleaned_data['province']
            work_a = form.cleaned_data['work_a']
            work_b = form.cleaned_data['work_b']
            work_c = form.cleaned_data['work_c']

            update = m.Post.objects.create(
                user=user,
                date_of_birth=date_of_birth,
                skill=skill,
                education=education,
                city=city,
                province=province,
                work_a=work_a,
                work_b=work_b,
                work_c=work_c)

            return HttpResponseRedirect(reverse('user_cv',
                kwargs={'cv_id': update.id}))   

    return render(request, '/edit_cv.html', {
        'form': form,
        }, context_instance=RequestContext(request))