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

def activity(request):
    return render(request,'alumniportal/activities.html', {'page': 'activity'})

def community(request):
    return render(request,'alumniportal/communities.html', {'page': 'community'})

def news(request):
    admin_posts = models.News.objects
    news = admin_posts.all()[:2]
    achievements = admin_posts.filter(post_type = 'C')[:2]
    return render(request,'alumniportal/news.html', {
        'page': 'news',
        'news':news,
        'achievements':achievements,
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
        })
