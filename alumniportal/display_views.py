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

####To pass the required recent objects
def get_recent_objects():
    pass   

def home(request):
    recent = models.Recent.objects.all()[0]
    researchs = recent.posts.filter(post_type='R')[:2]
    activities = recent.activities.all()[:2]
    volunteers = recent.activities.filter(activity_type = 'Volunteering')
    community = recent.posts.all()[0] 
    return render(request,'alumniportal/main-body.html', {
        'page': 'home',
        'researchs':researchs,
        'activities':activities,
        'volunteers':volunteers,
        'community':community,
        })

def activity(request):
    return render(request,'alumniportal/activities.html', {'page': 'activity'})

def community(request):
    return render(request,'alumniportal/communities.html', {'page': 'community'})

def news(request):
    recent = models.Recent.objects.all()[0]
    research = recent.posts.filter(post_type='R')[0]
    news = recent.posts.exclude(post_type='B')[:2]
    achievement = recent.achievements.all()[0]
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
    admin_blog = User.objects.get(username = ADMIN_USERNAME).profile.blog
    posts = models.Post.objects.filter(blog = admin_blog)
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
