#####DO NOT CLOSE WINDOW
from alumniportal import forms
from alumniportal import models
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q
import time
from datetime import datetime
from constants import *

####To pass the required recent objects in required numbers
def get_recent_objects():
    pass

def home(request):
    research = models.News.objects.filter(post_type = 'R').first()
    activities = models.Activity.objects
    activity = activities.first()
    volunteer = activities.filter(activity_type = 'V')
    community = models.Post.objects.first() #When Clubs get implemented change Post to ClubPosts (there would be some more changes too)
    return render(request,'alumniportal/main-body.html', {
        'page': 'home',
        'research':research,
        'activity': activity,
        'volunteer':volunteer,
        'community':community,
        })

def volunteer(request):
    volunteers = models.Activity.objects.filter(activity_type = 'V')
    return render(request, 'alumniportal/volunteer.html', {
        'page':'volunteer',
        'volunteers':volunteers,
        })

def activity(request):
    activities = models.Activity.objects.exclude(activity_type = 'V')
    return render(request,'alumniportal/activity.html', {
        'page': 'activity',
        'items':activities,
        'item_type':"ALL",
        })

def activity_items(request, item_type):
    for a in ACTIVITY_TYPE:
        if a[1]==item_type:
            activities = models.Activity.objects.filter(activity_type=a[0])
            return render(request, 'alumniportal/activity.html', {
                'page':'activity',
                'items':activities,
                'item_type':item_type,
                })
    return HttpResponseRedirect('/activity')

def community(request):
    post = models.Post.objects.first()
    return render(request,'alumniportal/communities.html', {
        'page': 'community',
        'post':post,
        })

def news(request):
    admin_posts = models.News.objects
    news = admin_posts.all()[:2]
    achievements = admin_posts.filter(post_type = 'C')[:2]
    return render(request,'alumniportal/news.html', {
        'page': 'news',
        'news':news,
        'achievements':achievements,
        'is_admin': request.user.is_superuser,
        })

@login_required
def profile(request):
    try:
        profile = models.Profile.objects.get(user = request.user)
    except:
        messages.error(request, "You can access profile unless you create your own profile.")
        return HttpResponseRedirect('/edit-profile')
    # import pdb; pdb.set_trace()
    return render(request,'alumniportal/profile.html', {
        'page': 'profile',
        'profile':profile,
        })

@login_required
def view_profile(request, profile_id):
    profile = User.objects.get(username = profile_id).profile
    return render(request,'alumniportal/profile.html', {
        'page': 'profile',
        'profile':profile,
        })

def items(request, class_type, item_type):
    #####need to add continuously loading of news
    news = models.News.objects.all()
    print request.path
    # print POST_TYPE
    if class_type == "news":
        items = news
        for a in POST_TYPE:
            if a[1] == item_type:
                items = news.filter(post_type = a[0])

    ########WHat happens if none of the URL matches!!!!
    return render(request,'alumniportal/news-list.html', {
        'page': 'items',
        'items':items,
        'item_type':item_type,
        'is_admin': request.user.is_superuser,
        })

ignoreField = ['company']
@login_required
def createQuery(queryset, result, field):
    result = result | Q(**{field + "__icontains" : queryset[field]})
    return result

@login_required
def search(request):
    profiles = []
    if request.POST:
        query = Q()
        queryset = request.POST.copy()
        past_company = queryset['company']
        past_education = queryset['institute']
        if queryset['name']:
            list_of_words = queryset['name'].split()
            for word in list_of_words:
                query = query | Q(name__icontains = word)
        
        del queryset['company']
        del queryset['csrfmiddlewaretoken']
        del queryset['institute']
        del queryset['name']
        
        for field in queryset:
            if queryset[field]:
                query = createQuery(queryset, query, field)
        if past_company:
            query = query | Q(jobs__company__icontains = past_company)
        if past_education:
            query = query | Q(educations__institute__icontains = past_education)

        # import pdb; pdb.set_trace()
        profiles = models.Profile.objects.filter(query).distinct()
        # kj
        print query
        print profiles
    return render(request, 'alumniportal/search.html', {
        'page':"search",
        'batches':PASS_OUT_YEARS,
        'majors':DEPARTMENTS,
        'hostels':HOSTELS,
        'profiles':profiles,
        'hostels':HOSTELS,
        })


def news_detail(request, news_id):
    news = models.News.objects.get(id=news_id)
    return render(request, 'alumniportal/news-detail.html', {
        'page': 'news-detail',
        'heading': news.heading,
        'content': news.content,
        'news_id': news.id,
        'is_admin': request.user.is_superuser,
        })

@login_required(login_url='/login/')
def blog(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponse('Username does not exist.')
    blog = user.profile.blog
    posts = blog.post_set.all()
    return render(request,'alumniportal/blog.html', {
        'page': 'items',
        'posts': posts,
        'is_editor': (blog.profile.user == request.user),
        'username': user.username,
        })

@login_required(login_url='/login/')
def post_detail(request, username, post_id):
    post = models.Post.objects.get(id=post_id)
    if post.blog.profile.user.username != username:
        return HttpResponse('User post mismatch error. Please report to'
                            'administrators if this error persists.')
    return render(request, 'alumniportal/post-detail.html', {
        'page': 'post-detail',
        'heading': post.heading,
        'content': post.content,
        'post_id': post.id,
        'is_editor': (post.blog.profile.user == request.user),
        'username': username,
        })
