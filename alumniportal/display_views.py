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
def home(request):
    return render(request,'alumniportal/main-body.html', {'page': 'home'})

def activity(request):
    return render(request,'alumniportal/activities.html', {'page': 'activity'})

def community(request):
    return render(request,'alumniportal/communities.html', {'page': 'community'})

def news(request):
    admin_blog = User.objects.get(username = ADMIN_USERNAME).profile.blog
    posts = models.Post.objects.filter(blog = admin_blog).exclude(post_type = 'B')[:2]
    # import pdb; pdb.set_trace()
    # print news[0]
    # print news[1]
    # print news   
    return render(request,'alumniportal/news.html', {
        'page': 'news',
        'news':posts,
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

def news_list(request):
    return render(request,'alumniportal/news-list.html', {'page': 'news-list'})
