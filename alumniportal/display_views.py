#####DO NOT CLOSE WINDOW
from alumniportal import forms
from alumniportal import models
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
import time
from datetime import datetime
from constants import *

####To pass the required recent objects in required numbers
def get_recent_objects():
    pass   

def home(request):
    admin_blog = User.objects.get(username = ADMIN_USERNAME).profile.blog
    posts = models.Post.objects.filter(blog = admin_blog)
    researchs = posts.filter(post_type = 'R')[:2]
    activities = models.Activity.objects
    volunteer = activities.filter(activity_type = 'Volunteering').first()
    activities = activities.all()[:2]
    community = models.Post.objects.first()
    return render(request,'alumniportal/main-body.html', {
        'page': 'home',
        'researchs':researchs,
        'activities':activities,
        'volunteer':volunteer,
        'community':community,
        })

def activity(request):
    return render(request,'alumniportal/activities.html', {'page': 'activity'})

def community(request):
    return render(request,'alumniportal/communities.html', {'page': 'community'})

def news(request):
    achievement = models.Achievement.objects.first()
    admin_blog = User.objects.get(username = ADMIN_USERNAME).profile.blog
    posts = models.Post.objects.filter(blog = admin_blog)
    news = posts.exclude(post_type = 'B')[:2]
    research = posts.filter(post_type = 'R').first()
    return render(request,'alumniportal/news.html', {
        'page': 'news',
        'news':news,
        'research':research,
        'achievement':achievement,
        })

@login_required
def profile(request):
    try:
        profile = models.Profile.objects.get(user = request.user)
    except:
        return HttpResponseRedirect('/edit-profile')
    return render(request,'alumniportal/profile.html', {
        'page': 'profile',
        'profile':profile,
        })

def items(request, class_type, item_type):
    #####need to add continuously loading of news
    posts = models.News.objects.all()
    print request.path
    if class_type == "news":
        if item_type == "all":
            items = posts.exclude(post_type = 'B')
        elif item_type == "research":
            items = posts.filter(post_type = 'R')
        elif item_type == "iitg":
            items = posts.filter(post_type = 'I')
        elif item_type == "student":
            items = posts.filter(post_type = 'S')
    elif class_type == "achievement":
        achievements = models.Achievement.objects.all()
        if item_type == "all":
            items = achievements
        elif item_type == "alumni":
            items = achievements.filter(achievement_type = 'A')
        elif item_type == "student":
            items = achievements.filter(achievement_type = 'S')
        elif item_type == "iitg":
            items = achievements.filter(achievement_type = 'I')
    ########WHat happens if none of the URL matches!!!!
    return render(request,'alumniportal/news-list.html', {
        'page': 'items',
        'items':items,
        'class_type':class_type,
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
